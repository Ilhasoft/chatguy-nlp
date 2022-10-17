FROM python:3.8.13-slim

WORKDIR /home/

ENV POSTGRES_USER postgres
ENV POSTGRES_HOST postgres_db
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_PORT 5432
ENV POSTGRES_ADAPTER postgresql

COPY Chatguy /home/Chatguy
COPY requirements-dev.txt /home

RUN apt update
RUN apt-get install -y libpq-dev
RUN pip install -r requirements-dev.txt --no-cache-dir

#RUN python /home/Chatguy/create_db.py
