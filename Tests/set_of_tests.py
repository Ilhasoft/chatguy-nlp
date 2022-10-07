from Tests.test_api_fuctions import *
from Tests.test_config import user_input_word, word_synonym_res
import sys, os
from os.path import dirname, join, abspath

#sys.path.insert(1, abspath(join(dirname(__file__), '..')))

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

class TestsEnsemble:
    def __init__(self):
        self.name = 1 
        self.input = 2
        self.output = 3
        pass

all_tests = [
{"Test_word_generator": test_word_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},

{"Test_sentence_generator": test_sentence_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},

{"Test_store_corrections": test_word_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},

{"Test_get_synonymous": test_word_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},

{"Test_word_generator": test_word_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},

{"Test_word_generator": test_word_generator_function,
"inputs": test_word_generator_function(user_input_word.texts),
"output": word_synonym_res},


]