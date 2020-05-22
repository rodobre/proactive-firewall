FROM ubuntu

RUN apt -y update
RUN apt -y install python3 python3-pip
RUN python3 -m pip install flask

WORKDIR /react_app/

CMD ["python3", "-u", "./backend/app.py"]
EXPOSE 5000
