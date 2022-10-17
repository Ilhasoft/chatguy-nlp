from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Date, Table, MetaData, ForeignKey, join
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc
import os

Base = declarative_base()

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
adapter = os.environ['POSTGRES_ADAPTER']

DATABASE_URL = f'{adapter}://{user}:{password}@{host}:{port}'

# create an engine
engine = create_engine(DATABASE_URL)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
meta = MetaData()

words = Table('words', meta, Column('id', Integer, primary_key=True), Column('word', String, unique=True),)
suggestions = Table('suggestions', meta, Column('id', Integer, primary_key=True), Column('id_word', Integer, ForeignKey('words.id')), Column('suggestion', String),)
corrections = Table('corrections', meta, Column('id', Integer, primary_key=True), Column('source_text', String), Column('target_text', String),)
meta.create_all(engine)
