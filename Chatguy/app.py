import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import InputCorrections, InputSentences, InputWords
import csv
from handlers import classifier, db, text_generators
import logging
import sqlalchemy
import os
import urllib.request
from sqlalchemy import Column, Integer, MetaData, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.orm import sessionmaker
from handlers.try_except import error_handling
from functools import wraps
from fastapi import APIRouter

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


@router.post(r'/suggest_words/')
@error_handling
def suggest_words(userInput: InputWords):
    if userInput:
        session = db.create_db(DATABASE_URL)
        keys = userInput.texts
        result_word = text_generators.generate_words(keys, session)
        session.close()
    return result_word


@router.post(r'/suggest_sentences/')
@error_handling
def suggest_sentences(userInput: InputSentences):
        if userInput.texts:
            result_sentence = text_generators.generate_sentences(userInput)
        return result_sentence


@router.post(r'/store_corrections/')
@error_handling
def suggest_words(userInput: InputCorrections):
        if userInput:
            session = db.create_db(DATABASE_URL)
            data = userInput.texts
            db.insert_corrections(session, data[0], data[1])
            session.close()
            return {200: 'Inserted!'}



