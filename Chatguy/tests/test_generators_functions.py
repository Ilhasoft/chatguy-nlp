from app import DATABASE_URL
import pytest
import json
#from fastapi.testclient import TestClient
from models.models import InputSentences
from handlers import text_generators, db, classifier
from pydantic import BaseModel
import pysinonimos
from pysinonimos import sinonimos
from pysinonimos.sinonimos import Search, historic
#from test_api import dotdict, userInput, bg_res
#from test_api import  DATABASE_URL, user, password, host, port, adapter
#from create_db import adapter
# import create_db


# Simple test 1
def test_one_plus_five():
    assert 1 + 5 == 6


def func(x):
    return x + 1

# Simple test 2
def test_answer():
    assert func(3) == 4

# Test 3
def test_get_synonyms_word_not_null():
    word = 'teste'
    print(word)
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert Search(word) != Search(' ')
    

synonyms_teste = ['avaliação', 'exame', 'prova',
'provação', 'verificação', 'constatação', 'ensaio',
'experiência', 'experimentação', 'experimento',
'investida', 'tentativa', 'mostragem']

def test_get_word_equals_suggested_synonyms():
    word = 'teste'
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert suggested == synonyms_teste

synonyms_caderno = ['caderneta', 'livrete', 'seção',
'suplemento', 'brochura', 'fascículo', 'folheto',
'livro', 'bloco', 'agenda']

def test_get_word_equals_suggested_synonyms():
    word = 'caderno'
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert suggested == synonyms_caderno

def test_list_suggesting(key):
    ...

'''
def test_word_generator():
    print(userInput.texts)
    print('hi this is a test')
    session = db.create_db(DATABASE_URL)
    keys = userInput.texts
    result_word = text_generators.generate_words(keys, session)
    session.close()
    assert result_word == bg_res


# Test Generate Sentence - Test 3
def test_sentence_generator():
    print('hi this is a test')
    print(userInput.texts)
    session = db.create_db(DATABASE_URL)
    keys = userInput.texts
    result_sentence = text_generators.generate_words(keys, session)
    session.close()
    assert result_sentence == bg_res
'''


