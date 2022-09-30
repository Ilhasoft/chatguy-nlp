import json
import pytest
from test_config import *
from handlers import text_generators, db
from app import *
from create_db import DATABASE_URL
from types import SimpleNamespace
import sys
import os
import pysinonimos
from test_config import *
from pkg_resources import NullProvider
from handlers import classifier
from pydantic import BaseModel
from pysinonimos import sinonimos
from pysinonimos.sinonimos import Search, historic
#from test_config import user_input_word, word_synonym_res, user_input_sentence, sentence_res, user_input_corrections, result_corrections_res
from models.models import InputWords, InputSentences, InputCorrections

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
adapter = os.environ['POSTGRES_ADAPTER']

DATABASE_URL = f'{adapter}://{user}:{password}@{host}:{port}'


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

user_input_word = dotdict(user_input_word)
user_input_sentence = dotdict(user_input_sentence)
user_input_corrections = dotdict(user_input_corrections)

#userInput = json.dumps(userInput)
#userInput = json.loads(userInput, object_hook=lambda d: SimpleNamespace(**d))

def test_word_generator_function():
    print('hi')
    print(user_input_word.texts)
    session = db.create_db(DATABASE_URL)
    keys = user_input_word.texts
    result_word = text_generators.generate_words(keys, session)
    session.close()

    assert result_word == word_synonym_res
    assert isinstance(result_word, list)
    #assert text_generators.generate_words(keys, session) == 5


def test_sentence_generator_function():
    print('Sentence Generator Test\n')
    session = db.create_db(DATABASE_URL)
    key = user_input_sentence
    result_sentence = text_generators.generate_sentences(key)
    session.close()

    assert result_sentence == sentence_res
    assert isinstance(result_sentence, dict)
    

@pytest.mark.skip(reason='not ready, WIP')
def test_store_corrections():
    '''
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    '''
    session = db.create_db(DATABASE_URL)
    data = user_input_corrections
    print('Store Corrections test \n')
    data[0] = data['texts'][0]
    data[1] = data['texts'][1]
    result_corrections = db.insert_corrections(session, data[0], data[1])
    print(data[0])
    print(data[1])
    print(result_corrections)
    session.close()
    assert result_corrections == result_corrections_res

@pytest.mark.skip(reason='not ready, WIP')
def test_store_corrections_2():
    '''
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    '''
    session = db.create_db(DATABASE_URL)
    data = user_input_corrections
    result_corrections = db.insert_corrections(session, data[0], data[1])
    print(type(data[0]))
    print(type(data[1]))
    print(type(data))
    print(result_corrections)
    session.close()
    assert result_corrections == result_corrections_res 
    
def test_one_plus_five():
    '''
    Teste base - verificar funcionamento
    '''
    assert 1 + 5 == 6


def test_get_synonyms_word_not_null():
    '''
    Test synonyms words
    '''
    word = 'teste'
    print(word)
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert Search(word) != Search(' ')
    

def test_get_word_equals_suggested_synonyms():
    '''
    Test synonyms words output
    '''
    word = 'teste'
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert suggested == synonyms_teste


def test_get_word_equals_suggested_synonyms():
    '''
    Test synonyms words output
    '''
    word = 'caderno'
    suggested = Search(word)
    suggested = suggested.synonyms()
    print(suggested)
    assert suggested == synonyms_caderno

@pytest.mark.skip(reason = 'not ready - WIP')
def test_list_suggesting(key):
    print('test list suggesting')
    new_arr = []
    for i in range(len(key)):
        new_arr.append(key[i]['suggestions'])
    arr_new = list(itertools.product(*new_arr))
    result = map(join_tuple_string, list(arr_new))
    return list(result)

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model_gec():
    print('test create model gec')

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model():
    print('test create model')

def test_join_tuple_string():
    print('test join tuple string | param = strings_tuple')

def test_phrase_gec():
    print('test phrase gec | param = list_phrases, model')

def test_phrase_aug():
    print('test phrase aug | param = uggest_list, pten_pipeline, enpt_pipeline')
