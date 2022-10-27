from codecs import backslashreplace_errors
from imghdr import tests
import sys

from models.models import Recover

sys.path.insert(1, '..')

import json
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from Chatguy.models.models import InputCorrections, InputSentences, InputWords
import csv
from Chatguy.handlers import classifier, db, text_generators, try_except, try_except
from tests import test_api_functions, test_config
from tests.test_config import TimedRoute, log_datetime, timer, StoreCorrections, word_synonym_res, sentence_res
import logging
import sqlalchemy
import os, sys
import urllib.request
from sqlalchemy import Column, Integer, MetaData, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.orm import sessionmaker
from functools import wraps
import json
import redis
import base64
from hashlib import blake2b
import time

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
adapter = os.environ['POSTGRES_ADAPTER']

client = TestClient(router)

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
@timer
def suggest_words(userInput: InputWords):
    if userInput:
        session = db.create_db(DATABASE_URL)
        keys = userInput.texts
        result_word = text_generators.generate_words(keys, session)
        session.close()
    return result_word


@router.post(r'/suggest_sentences/')
@try_except.error_handling
def suggest_sentences(userInput: InputSentences, background_tasks: BackgroundTasks):
        if userInput.texts:            
            token = gen_token()
            background_tasks.add_task(gen_sentences, userInput, token) 
        return token


@router.post(r'/recover_sentences/')
@try_except.error_handling
def application_test(id: Recover, background_tasks: BackgroundTasks):
    if not r.get(id.token):
        return None
    msg_bytes = base64.b64decode(r.get(id.token))
    msg_bytes = msg_bytes.decode('ascii')
    background_tasks.add_task(del_token, id.token) 
    return json.loads(msg_bytes)


@router.post(r'/store_corrections/')
@try_except.error_handling
def suggest_words(userInput: InputCorrections):
        if userInput:
            session = db.create_db(DATABASE_URL)
            data = userInput.texts
            db.insert_corrections(session, data[0], data[1])
            session.close()
            return {200: 'Inserted!'}


router.route_class = TimedRoute

@router.post(r'/tests/')
@try_except.error_handling
@log_datetime
def test_application_route():
    runtime_route_words = test_api_functions.test_route_suggets_words()
    runtime_route_sentence = test_api_functions.test_route_suggets_sentence()
    runtime_route_words = test_api_functions.test_route_store_corrections()
    runtime_route_recover = test_api_functions.test_route_recover_sentences()

    return {'Route Name -->': ('Suggest Words', 'Suggest Sentences', 'Store Corrections', 'Recover Sentences'),
            'Runtime': (runtime_route_words, runtime_route_sentence, runtime_route_words, runtime_route_recover)}

