from os.path import dirname, join, abspath
from lib2to3.pgen2.token import EQUAL
from tkinter import Y
import pytest
import json
import sys
import os
from ..Chatguy import *
import Tests.test_config as test_config
import itertools
from ..Chatguy.handlers import db, text_generators, classifier
from ..Chatguy.models.models import InputWords, InputSentences, InputCorrections
from types import SimpleNamespace
from simplet5 import SimpleT5
import SimpleT5 
from pkg_resources import NullProvider
from pydantic import BaseModel
from pysinonimos import sinonimos

from ..Chatguy.models.models import Search, historic, pysinonimos, sinonimos
from Tests.test_config import StoreCorrections


sys.path.insert(1, abspath(join(dirname(__file__), '..')))
sys.path.insert(0, abspath(join(dirname(__file__), '.')))
sys.path.insert(os.path.join(os.path.abspath(os.path.dirname(__file__), '..', '.')))

'''myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
print(myPath)'''



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

user_input_word = dotdict(test_config.user_input_word)
user_input_sentence = dotdict(test_config.user_input_sentence)
user_input_corrections = dotdict(test_config.user_input_corrections)

#userInput = json.dumps(userInput)
#userInput = json.loads(userInput, object_hook=lambda d: SimpleNamespace(**d))


def test_word_generator_function():
    print('hi')
    print(user_input_word.texts)
    session = db.create_db(DATABASE_URL)
    keys = user_input_word.texts
    result_word = text_generators.generate_words(keys, session)
    session.close()

    assert result_word == test_config.word_synonym_res
    assert isinstance(result_word, list)
    #assert text_generators.generate_words(keys, session) == 5


def test_sentence_generator_function():
    print('Sentence Generator Test\n')
    session = db.create_db(DATABASE_URL)
    key = user_input_sentence

    result_sentence = text_generators.generate_sentences(key)
    session.close()

    assert result_sentence == test_config.sentence_res
    assert isinstance(result_sentence, dict)
    

def test_store_corrections():
    '''
    Test to ensure the correct inclusion of fixes in the database connection
    '''
    session = db.create_db(DATABASE_URL)
    data = user_input_corrections.texts

    db.insert_corrections(session, data[0], data[1])

    query_result = db.query_corrections(session)
  
    banco = StoreCorrections()
    banco.id = query_result [0].id
    banco.source_text = query_result[0].source_text
    banco.target_text = query_result[0].target_text

    session.close()
    
    assert banco.id == test_config.result_corrections_res.id, 'ID is not the same'
    assert banco.source_text == test_config.result_corrections_res.source_text, 'Source text is not the same'
    assert banco.target_text == test_config.result_corrections_res.target_text, 'Target text is not the same'


def test_get_synonyms_word_not_null():
    '''
    Test synonyms words
    '''
    word = 'teste'
    print(word)
    suggested = Search(word)
    suggested = suggested.synonyms()

    assert Search(word) != Search(' ')
    

def test_get_word_equals_suggested_synonyms():
    '''
    Test synonyms words output
    '''
    word = 'teste'
    suggested = Search(word)
    suggested = suggested.synonyms()
    
    assert suggested == test_config.synonyms_teste


def test_get_word_equals_suggested_synonyms():
    '''
    Test synonyms words output
    '''
    word = 'caderno'
    suggested = Search(word)
    suggested = suggested.synonyms()
    
    assert suggested == test_config.synonyms_caderno


def test_list_suggesting():
    '''
    Test list suggesting output
    '''
    key = user_input_sentence.texts
    suggested_list = classifier.list_suggesting(key)
    
    print('test list suggesting', suggested_list)
    print('\ntest consfig sentence res', test_config.sentence_res)

    assert isinstance(suggested_list, list)
    assert suggested_list == test_config.res_suggested_list


def test_join_tuple_string():
    '''
    Test join tuple String
    '''
    print('test join tuple string | param = strings_tuple')
    string = ('teste', 'teste', 'teste')

    join_tuple_str = classifier.join_tuple_string 
    result_join = join_tuple_str(string)
    print(result_join)

    assert result_join == str('teste teste teste')

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_gec():
    ''''''
    print('test phrase gec | param = list_phrases, model')
    list_phrases = ['teste']
    model = classifier.create_model_gec() 
    phrase_gec = classifier.phrase_gec(list_phrases, model)

    print(phrase_gec, model)

    assert isinstance(phrase_gec, list)

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_aug():
    ''''''
    print('test phrase aug | param = suggest_list, pten_pipeline, enpt_pipeline')
    suggest_list  = classifier.list_suggesting()
    pten_pipeline, enpt_pipeline = classifier.create_model()

    aug_list = classifier.phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
    assert isinstance(aug_list, list)


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model_gec():
    ''''''
    print('test create model gec')
    model = SimpleT5()
    model.load_model("t5",'./model', use_gpu=False)
    
    return model


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model():
    ''''''
    print('test create model')
