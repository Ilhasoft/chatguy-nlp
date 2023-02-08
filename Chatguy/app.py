import sys
import os

from models.models import Recover
sys.path.insert(1, '..')

import json
import csv
import logging
import sqlalchemy
import urllib.request
import redis
import base64
import time
from codecs import backslashreplace_errors
from http.cookies import SimpleCookie
from imghdr import tests
from signal import Handlers
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from Chatguy.models.models import InputCorrections, InputSentences, InputWords
from Chatguy.handlers import classifier, db, text_generators, try_except, try_except
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, MetaData, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from functools import wraps
from hashlib import blake2b


r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

logging.basicConfig(
    filename='logfile.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger()

router = FastAPI()


origins = ["*"]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']


DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}'
session = db.create_db(DATABASE_URL)

def gen_sentences(userInput, token):
    resul = json.dumps(text_generators.generate_sentences(userInput))
    message = str(resul)
    ascii_message = message.encode('ascii')
    output_byte = base64.b64encode(ascii_message)
    r.set(token, output_byte)


def gen_token(token=None):
    while True:
        k = str(time.time()).encode('utf-8')
        h = blake2b(key=k, digest_size=16)
        if not r.get(h.hexdigest()):
            return h.hexdigest()


def del_token(token):
    r.delete(token)


@router.post(r'/suggest_words/')
@try_except.error_handling
def suggest_words(userInput: InputWords):
    if userInput:
        print('A')
        session = db.create_db(DATABASE_URL)
        print('B')
        keys = userInput.texts
        print('C')
        result_word = text_generators.generate_words(keys, session)
        print('I')
        session.close()
    return result_word


@router.post(r'/suggest_sentences/')
@try_except.error_handling
def suggest_sentences(userInput: InputSentences, background_tasks: BackgroundTasks):
        if userInput.texts:
            print('J')            
            token = gen_token()
            print('K')   
            background_tasks.add_task(gen_sentences, userInput, token)
            print('L')    
        return token



@router.post(r'/recover_sentences/')
@try_except.error_handling
def application_test(id: Recover, background_tasks: BackgroundTasks):
    if not r.get(id.token):
        print('M')   
        return None
    msg_bytes = base64.b64decode(r.get(id.token))
    print('N', msg_bytes)   
    msg_bytes = msg_bytes.decode('ascii')
    print('O')   
    background_tasks.add_task(del_token, id.token)   
    return json.loads(msg_bytes)


@router.post(r'/store_corrections/')
@try_except.error_handling
def suggest_words(userInput: InputCorrections):
        if userInput:
            print('P')   
            session = db.create_db(DATABASE_URL)
            print('Q')   
            data = userInput.texts
            print('R', data)   
            db.insert_corrections(session, data[0], data[1])
            print('S')   
            session.close()
            return {200: 'Inserted!'}



@router.post(r'/tests/')
@try_except.error_handling
def test_application_route():
    client = TestClient(router)

    import time


    '''class Performance:
        def __init__(self, func, *args):
            self.start = time.monotonic()
            self.running = func(*args)
            self.end = time.monotonic()
            self.run_time_route = self.end - self.start
            self.report = (f'Function: {self.func.__name__}',
                            f'\nTime elapsed is seconds: {self.end- self.start:.6f}',
                            f'{"-"*40}' )
    '''
                          

    def test_route_suggest_words_request():
        start_words = time.monotonic()
        response_words = client.post('/suggest_words/')
        end_words = time.monotonic()
        run_time_words = end_words - start_words
        word_report = ['Route: Suggest Words',
                            f'Function: {test_route_suggest_words_request.__name__}',
                            f'Request Status Code: {response_words.status_code}',
                            f'Time elapsed is seconds: {run_time_words:.6f}']
        return word_report


    def test_route_suggest_sentence_request():
        start_sent = time.monotonic()
        response_sent = client.post(r'/suggest_sentences/')
        end_sent = time.monotonic()
        run_time_sent = end_sent - start_sent
        sent_report = ['Route: Suggest Words',
                            f'Function: {test_route_suggest_sentence_request.__name__}',
                            f'Request Status Code: {response_sent.status_code}',
                            f'Time elapsed is seconds: {run_time_sent:.6f}']
        return sent_report


    def test_route_suggest_store_corrections_request():
        start_store = time.monotonic()
        response_store = client.post(r'/store_corrections/')
        end_store = time.monotonic()
        run_time_store = end_store - start_store
        store_report = ['Route: Suggest Words',
                            f'Function: {test_route_suggest_sentence_request.__name__}',
                            f'Request Status Code: {response_store.status_code}',
                            f'Time elapsed is seconds: {run_time_store:.6f}']
        return store_report


    def test_route_suggest_recover_sentence_request():
        start_recover = time.monotonic()
        response_recover = client.post(r'/recover_sentences/')
        end_recover = time.monotonic()
        run_time_recover = end_recover - start_recover
        recover_report = ['Route: Suggest Words',
                            f'Function: {test_route_suggest_sentence_request.__name__}',
                            f'Request Status Code: {response_recover.status_code}',
                            f'Time elapsed is seconds: {run_time_recover:.6f}']
        return recover_report


    return ({'Routes Report':([test_route_suggest_words_request()],
                            [test_route_suggest_sentence_request()],
                            [test_route_suggest_store_corrections_request()], 
                            [test_route_suggest_recover_sentence_request()]),
                            })