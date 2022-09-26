import pytest
from handlers import db, text_generators, try_except, try_except
from types import SimpleNamespace
import sys
import create_db
import os
from tests import test_config
from tests.test_config import user_input_word, word_synonym_res, user_input_sentence, sentence_res, user_input_corrections, result_corrections_res

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
adapter = os.environ['POSTGRES_ADAPTER']

DATABASE_URL = f'{adapter}://{user}:{password}@{host}:{port}'

sys.path.insert(0, '/home/mel/chatguy-nlp/Chatguy/handlers/text_generators.py')
sys.path.insert(1, '/home/mel/chatguy-nlp/Chatguy/handlers/try_except.py')
sys.path.insert(2, '/home/mel/chatguy-nlp/Chatguy/app.py')

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

user_input_word = dotdict(user_input_word)
user_input_sentence = dotdict(user_input_sentence)

#userInput = json.dumps(userInput)
#userInput = json.loads(userInput, object_hook=lambda d: SimpleNamespace(**d))

def test_word_generator_function():
    print('hi')
    print(user_input_word.texts)
    session = db.create_db(DATABASE_URL)
    keys = user_input_word.texts
    result = text_generators.generate_words(keys, session)
    session.close()
    assert result == word_synonym_res
    #assert text_generators.generate_words(keys, session) == 5


def test_sentence_generator_function():
    print('hi this is a test')
    print(user_input_sentence.texts)
    session = db.create_db(DATABASE_URL)
    key = user_input_sentence
    result_sentence = text_generators.generate_sentences(key)
    session.close()
    assert result_sentence == sentence_res()


def test_store_corrections():
    '''
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    '''
    session = db.create_db(DATABASE_URL)
    data = user_input_corrections
    result_corrections = db.insert_corrections(session, data[1], data[2])
    session.close()
    assert result_corrections == result_corrections_res

