FROM python:3.8.13-slim

WORKDIR /home/

COPY Chatguy /home/Chatguy
COPY requirements.txt /home


RUN pip install -r requirements.txt --no-cache-dir

WORKDIR /home/Chatguy
#CMD ["uvicorn","app:router","host=0.0.0.0","port=8000", "--reload"]
CMD ["uvicorn", "app:router", "--host", "0.0.0.0", "--port", "8000","--reload" ]