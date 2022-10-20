FROM python:3.8.13-slim

WORKDIR /home/

COPY Chatguy /home/Chatguy
COPY requirements.txt /home

RUN apt update
RUN apt-get install -y libpq-dev
RUN apt-get install -y redis-server

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /home/Chatguy
RUN mkdir -p /home/Chatguy/model

CMD sh -c 'redis-server --appendonly yes --appendfsync no & exec uvicorn app:router --host 0.0.0.0 --port 8000 --reload'
