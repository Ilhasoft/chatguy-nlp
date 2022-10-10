from tests.test_api_fuctions import *
from tests.test_config import user_input_word, word_synonym_res
import sys, os
from os.path import dirname, join, abspath

path = sys.path.append(os.path.abspath(os.path.dirname(__file__)+"/.."))
print('path - set os tests\n',os.path.abspath(os.path.dirname(__file__)))
print('path - set os tests 2\n', os.path.abspath(os.path.pardir))


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