from app import DATABASE_URL
import pytest
import json
from models.models import InputSentences
from handlers import text_generators, db, classifier
from pydantic import BaseModel
import pysinonimos
from pysinonimos import sinonimos
from pysinonimos.sinonimos import Search, historic
from tests.test_config import synonyms_teste, synonyms_caderno


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

def test_list_suggesting():
    print('test list suggesting')

def test_create_model_gec():
    print('test create model gec')

def test_create_model():
    print('test create model')

def test_join_tuple_string():
    print('test join tuple string | param = strings_tuple')

def test_phrase_gec():
    print('test phrase gec | param = list_phrases, model')

def test_phrase_aug():
    print('test phrase aug | param = uggest_list, pten_pipeline, enpt_pipeline')
