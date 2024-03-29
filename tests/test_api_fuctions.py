import pytest
import sys
import os
import json
import tests.test_config as test_config
import itertools
from pkg_resources import NullProvider
from lib2to3.pgen2.token import EQUAL
from tkinter import Y
from types import SimpleNamespace
sys.path.insert(1, '..')
from Chatguy.models.models import InputWords, InputSentences, InputCorrections
from Chatguy.handlers.db import Base, Words, Suggestions, Corrections, create_db, create_word, create_suggestion, insert_corrections, query_corrections
from Chatguy.handlers.text_generators import generate_sentences, generate_words
from Chatguy.handlers.classifier import join_tuple_string, list_suggesting, get_synonyms, create_model_gec, create_model, phrase_aug, phrase_gec
from types import SimpleNamespace
from tests.test_config import StoreCorrections, user_input_corrections, user_input_sentence, user_input_word, word_synonym_res, sentence_res, synonyms_caderno, synonyms_teste, res_suggested_list
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


def test_word_generator_function():
    '''
    Test to verify that the generation of synonyms for words is correct.
    '''
    print(user_input_word.texts)
    session = create_db(DATABASE_URL)
    keys = user_input_word.texts
    result_word = generate_words(keys, session)
    session.close()

    assert result_word == test_config.word_synonym_res
    assert isinstance(result_word, list)
    #assert text_generators.generate_words(keys, session) == 5


def test_sentence_generator_function():
    '''
    Test to verify that the sentence generation is correct.
    '''
    session = create_db(DATABASE_URL)
    key = user_input_sentence

    result_sentence = generate_sentences(key)
    session.close()

    assert result_sentence == test_config.sentence_res
    assert isinstance(result_sentence, dict)
    

def test_store_corrections():
    '''
    Test to ensure the correct inclusion of fixes in the database connection
    '''
    session = create_db(DATABASE_URL)
    data = user_input_corrections.texts

    insert_corrections(session, data[0], data[1])

    query_result = query_corrections(session)
  
    banco = StoreCorrections()
    banco.id = query_result [0].id
    banco.source_text = query_result[0].source_text
    banco.target_text = query_result[0].target_text

    session.close()
    
    assert banco.id == test_config.result_corrections_res.id, 'ID is not the same'
    assert banco.source_text == test_config.result_corrections_res.source_text, 'Source text is not the same'
    assert banco.target_text == test_config.result_corrections_res.target_text, 'Target text is not the same'


def test_get_synonyms_word_type():
    '''
    test to check the input and output type of the synonym generator function.
    Input must be -> str 
    Output must be -> list
    '''
 
    suggested = Search(test_config.word)
    word_suggested = suggested.synonyms()

    assert type(test_config.word) == str, 'Input word is not string type'
    assert type(word_suggested) == list, 'suggest synonym is not list type'


def test_get_word_equals_suggested_synonyms():
    '''
    Test synonyms words output for input word 'teste' and 'caderno'
    '''

    suggested_word_1 = Search(test_config.word_1)
    suggested_word_2 = Search(test_config.word_2)

    suggested_1 = suggested_word_1.synonyms()
    suggested_2 = suggested_word_2.synonyms()
    
    assert suggested_1 == test_config.synonyms_teste
    assert suggested_2 == test_config.synonyms_caderno


def test_list_suggesting():
    '''
    Test list suggesting output
    '''
    key = user_input_sentence.texts
    suggested_list = list_suggesting(key)
    
    print('test list suggesting', suggested_list)
    print('\ntest consfig sentence res', test_config.sentence_res)

    assert isinstance(suggested_list, list)
    assert suggested_list == test_config.res_suggested_list


def test_join_tuple_string():
    '''
    Test join tuple String
    '''

    join_tuple_str = join_tuple_string 

    result_join = join_tuple_str(test_config.string)

    assert result_join == str('teste teste teste')


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_gec():
    '''
    '''    

    model = create_model_gec() 
    phrase_gec = phrase_gec(test_config.list_phrases, model)


    assert isinstance(phrase_gec, list)


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_phrase_aug():
    '''
    '''
    
    suggest_list  = list_suggesting()
    pten_pipeline, enpt_pipeline = create_model()

    aug_list = phrase_aug(suggest_list, pten_pipeline, enpt_pipeline)
    assert isinstance(aug_list, list)


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model_gec():
    '''
    '''
 
    model = SimpleT5()
    model.load_model("t5",'./model', use_gpu=False)
    
    return model


@pytest.mark.skip(reason = 'will be used after model implementation')
def test_create_model():
    '''
    '''
  
