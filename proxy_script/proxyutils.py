import math

def format_addr(addr):
	return '{}:{}'.format(addr[0], addr[1])

def small_hash(inp):
	base_hash = 917055679
	base_add = 382110149
	base_step = 2494664563
	base_mod = 4294967029

	back_inp = inp
	if isinstance(inp, list):
		back_inp = ''.join(inp)

	inp = back_inp

	for ch in inp:
		if isinstance(ch, str):
			ch = ord(ch)

		base_hash = ((base_hash & 0xffff) * ch) << 16 | ((base_hash >> 16) & 0xffff)
		base_hash = ((base_hash ^ base_add) + base_step) % base_mod

	return base_hash


def entropy(inp, base=2.0):
	if not inp:
		return 1.0

	table = dict.fromkeys(list(inp))
	freqvec = [float(inp.count(c)) / len(inp) for c in table]
	H = -sum([fr * math.log(fr) / math.log(base) for fr in freqvec])
	return H

colproto = {
	"HTTP": "\033[32mHTTP\033[0m",
	"HTTPS": "\033[36mHTTPS\033[0m",
	"WebSockets": "\033[31mWebSockets\033[0m",
	"TCP": "\033[19mTCP\033[0m"
}
