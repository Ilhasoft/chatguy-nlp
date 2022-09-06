FROM python:3.8.13-slim

WORKDIR /home/

COPY Chatguy /home/Chatguy
COPY requirements.txt /home

RUN sudo apt-get install -y libpq-dev
RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /home/Chatguy
RUN mkdir -p /home/Chatguy/model

CMD ["uvicorn", "app:router", "--host", "0.0.0.0", "--port", "8000","--reload" ]
