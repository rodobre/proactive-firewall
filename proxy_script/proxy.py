#!/usr/bin/python3
from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp
from mitmproxy import http
from mitmproxy import websocket

from proxyutils import format_addr
from proxyutils import colproto
from proxyutils import entropy
from proxyutils import small_hash

from RedisQueue import RedisQueue

import threading
import datetime as dt
import secrets
import time
import json

THREAD_SLEEP_TIME = 60

VERBOSE_LEVEL = 0
packets_dump = []


redis_packet_queue = None
redis_results_queue = None

methods = {
    'GET'    : 1,
    'HEAD'   : (1 << 1),
    'POST'   : (1 << 2),
    'PUT'    : (1 << 3),
    'DELETE' : (1 << 4),
    'CONNECT': (1 << 5),
    'OPTIONS': (1 << 6),
    'TRACE'  : (1 << 7),
    'PATCH'  : (1 << 8)
}

versions = {
    'HTTP/0.9': 1,
    'HTTP/1.0': (1 << 1),
    'HTTP/1.1': (1 << 2),
    'HTTP/2.0': (1 << 3)
}

schemes = {
    'http' : 1,
    'https': (1 << 1)
}

def http_connect(flow: http.HTTPFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["HTTPS"] + " [{} <- CONNECT ->]".format(
                format_addr(flow.client_conn.address))
        )

def request(flow: http.HTTPFlow):
    if VERBOSE_LEVEL == 1:
        if flow.server_conn.address:
            print(colproto["HTTP"] + " [{} -> {}]\t {}".format(
                    format_addr(flow.client_conn.address),
                    format_addr(flow.server_conn.address),
                    flow.request)
                )

def response(flow: http.HTTPFlow):
    global packets_dump
    global redis_queue
    global redis_packet_queue
    global redis_worker_queue

    if flow.server_conn and flow.response and flow.request:
        if VERBOSE_LEVEL == 1:
            print(colproto["HTTP"] + ' Parsing response and associated request')
            print(colproto["HTTP"] + ' Status code: {}'.format(flow.response.status_code))
            print(colproto["HTTP"] + ' Request method: {}'.format(flow.request.method))
            print(colproto["HTTP"] + ' HTTP version: {}'.format(flow.request.http_version))
            print(colproto["HTTP"] + ' HTTP scheme: {}'.format(flow.request.scheme))
            print(colproto["HTTP"] + ' Content length: {}'.format(len(flow.request.get_content())))

            print('Delta request time: {}'.format(flow.request.timestamp_end - flow.request.timestamp_start))
            print('Delta response time: {}'.format(flow.response.timestamp_end - flow.response.timestamp_start))
            print('Delta response - request: {}'.format(flow.response.timestamp_end - flow.request.timestamp_start))
            print('Port: {}'.format(flow.request.port))
            print('Client adress: {}'.format(flow.client_conn.ip_address))
            print('Server address: {}'.format(flow.server_conn.ip_address))
            print('{} {}'.format(dir(flow.client_conn), dir(flow.server_conn)))

            print('Request entropy: {}'.format(entropy(flow.request.content)))
            print('Response entropy: {}'.format(entropy(flow.response.content)))

        client_connection = format_addr(flow.client_conn.ip_address)
        server_connection = format_addr(flow.server_conn.ip_address)

        packet_to_add = [(flow.response.status_code, methods[flow.request.method],
                versions[flow.request.http_version], schemes[flow.request.scheme], len(flow.request.content),
                len(flow.response.content), entropy(flow.request.content), entropy(flow.response.content), small_hash(client_connection), small_hash(server_connection))]

        packets_dump.append(packet_to_add)
        
        # Send to proxy
        packet_msg = json.dumps({'packet':packet_to_add, 'id':secrets.randbits(256),                                              \
            'src':format_addr(flow.client_conn.ip_address).replace('::ffff:', ''), 'dst':format_addr(flow.server_conn.ip_address)})
        print('Enqueueing ', packet_msg, type(packet_msg))

        redis_packet_queue.put(packet_msg)


    if VERBOSE_LEVEL == 1:
        print(colproto["HTTP"] + " [{} <- {}]\t {}".format(
                format_addr(flow.client_conn.address),
                format_addr(flow.server_conn.address),
                flow.response)
        )

        print(colproto["HTTP"] + " Response -> {}\n{} Request -> {}\n".format(flow.response, colproto["HTTP"], flow.request))

def tcp_start(flow: tcp.TCPFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["TCP"] + " [{} <- HANDSHAKE -> {}]".format(
            format_addr(flow.client_conn.address),
            format_addr(flow.server_conn.address))
        )

def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]

    if VERBOSE_LEVEL == 1:
        print(colproto["TCP"] + " [{} -> {}]\t {}".format(
                format_addr(flow.client_conn.address) if message.from_client else format_addr(flow.server_conn.address),
                format_addr(flow.server_conn.address) if message.from_client else format_addr(flow.client_conn.address),
                message)
        )


def tcp_error(flow: tcp.TCPFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["TCP"] + " [{} <- ERROR -> {}]".format(
            format_addr(flow.client_conn.address),
            format_addr(flow.server_conn.address))
        )

def tcp_end(flow: tcp.TCPFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["TCP"] + " END [{} <-> {}]".format(
            format_addr(flow.client_conn.address),
            format_addr(flow.server_conn.address))
        )

def websocket_handshake(flow: http.HTTPFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["WebSockets"] + " [{} -> {}]\t {}".format(
                format_addr(flow.client_conn.address),
                format_addr(flow.server_conn.address),
                flow.request)
        )

def websocket_start(flow: websocket.WebSocketFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["WebSockets"] + " [{} ->]".format(
                format_addr(flow.client_conn.address))
        )

def websocket_message(flow: websocket.WebSocketFlow):
    message = flow.messages[-1]

    if VERBOSE_LEVEL == 1:
        print(colproto["WebSockets"] + " [{} -> {}]\t {}".format(
                format_addr(flow.client_conn.address) if message.from_client else format_addr(flow.server_conn.address),
                format_addr(flow.server_conn.address) if message.from_client else format_addr(flow.client_conn.address),
                message)
        )

def websocket_error(flow: websocket.WebSocketFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["WebSockets"] + " [{} <- ERROR -> {}]\t".format(
                format_addr(flow.client_conn.address),
                format_addr(flow.server_conn.address))
        )

def websocket_end(flow: websocket.WebSocketFlow):
    if VERBOSE_LEVEL == 1:
        print(colproto["WebSockets"] + " [{} <- END]".format(
                format_addr(flow.client_conn.address))
        )

# save the file as a csv
def save_as_csv(filename, columns, data):
    if not data or not columns:
        return
    with open(filename, 'w') as csv_out:
        for idx, column in enumerate(columns):
            csv_out.write(column)
            if idx != len(columns) - 1:
                csv_out.write(',')
        csv_out.write('\n')

        for idx, dat in enumerate(data):
            csv_out.write(repr(dat)[1:-1])
            csv_out.write('\n')

# the dump_traffic coroutine dumps information about proxied packets
def dump_traffic():
    global packets_dump
    global redis_packet_queue
    global redis_results_queue

    redis_packet_queue = RedisQueue('packet_worker_queue')
    redis_results_queue = RedisQueue('packet_results_queue')

    print('[*] Packet dumping thread is now online')
    while True:
        ts = time.time()
        date = dt.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H:%M:%S')
        save_as_csv('./packet_dump{}.csv'.format(date), ['Status code', 'Method', 'Version', 'Scheme', 'Request Length', 'Response Length', 'Request Entropy', 'Response Entropy', 'Client Connection', 'Server Connection'], packets_dump)
        time.sleep(THREAD_SLEEP_TIME)

traffic_dump = threading.Thread(target=dump_traffic)
traffic_dump.start()
