from tkinter import Y
import pytest
import json
import sys
import os
import test_config
import itertools
import handlers.db, handlers.text_generators, handlers.classifier
from models.models import InputWords, InputSentences, InputCorrections
from types import SimpleNamespace
from simplet5 import SimpleT5
from pkg_resources import NullProvider
from pydantic import BaseModel
from pysinonimos import sinonimos
from pysinonimos.sinonimos import Search, historic


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

def test_one_plus_five():

    assert 1 + 5 == 6


def test_word_generator_function():
    print('hi')
    print(user_input_word.texts)
    session = handlers.db.create_db(DATABASE_URL)
    keys = user_input_word.texts
    result_word = handlers.text_generators.generate_words(keys, session)
    session.close()

    assert result_word == test_config.word_synonym_res
    assert isinstance(result_word, list)
    #assert text_generators.generate_words(keys, session) == 5


def test_sentence_generator_function():
    print('Sentence Generator Test\n')
    session = handlers.db.create_db(DATABASE_URL)
    key = user_input_sentence
    result_sentence = handlers.text_generators.generate_sentences(key)
    session.close()

    assert result_sentence == test_config.sentence_res
    assert isinstance(result_sentence, dict)
    


#@pytest.mark.skip(reason='not ready, WIP')
def test_store_corrections():
    '''
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    '''
    session = handlers.db.create_db(DATABASE_URL)
    data = user_input_corrections.texts
    print(type(data), data)
    print(type(data[0]), data[0])
    print(type(data[1]), data[1])
   
    result_corrections = handlers.db.insert_corrections(session, data[0], data[1])
 
    print(type(result_corrections), result_corrections)
    session.close()
    
    assert result_corrections == test_config.result_corrections_res 


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

@pytest.mark.skip(reason='not ready, WIP')
def test_list_suggesting():
    ''''''
    key = user_input_sentence
    suggested_list = handlers.classifier.list_suggesting(key)
    
    print('test list suggesting', suggested_list)
    print('test list suggesting', test_config.sentence_res)
    print('test list suggesting', key)

    #assert isinstance(suggested_list, dict)
    assert suggested_list == test_config.sentence_res


def test_join_tuple_string():
    ''''''
    print('test join tuple string | param = strings_tuple')
    string = ('teste', 'teste', 'teste')
    join_tuple_str = handlers.classifier.join_tuple_string 
    result_join = join_tuple_str(string)
    print(result_join)

    assert result_join == str('teste teste teste')

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_gec():
    ''''''
    print('test phrase gec | param = list_phrases, model')
    list_phrases = ['teste']
    model = handlers.classifier.create_model_gec() 
    phrase_gec = handlers.classifier.phrase_gec(list_phrases, model)

    print(phrase_gec, model)

    assert isinstance(phrase_gec, list)

@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_aug():
    ''''''
    print('test phrase aug | param = suggest_list, pten_pipeline, enpt_pipeline')
    suggest_list  = handlers.classifier.list_suggesting()
    pten_pipeline, enpt_pipeline = handlers.classifier.create_model()

    aug_list = handlers.classifier.phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
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
