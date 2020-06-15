FROM ubuntu:latest

RUN apt -y clean
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3 python3-pip libmysqlclient-dev
RUN python3 -m pip install flask mysql-connector flask_cors

WORKDIR /react_app/

ENV MYSQL_USER threathunter
ENV MYSQL_PASSWORD Thr34THunT3R1sTh3B35tPr0DuCt

CMD ["python3", "-u", "./backend/app.py"]
EXPOSE 5000
