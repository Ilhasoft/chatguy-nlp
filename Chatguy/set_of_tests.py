from test_api_fuctions import *
from test_config import user_input_word, word_synonym_res
import sys



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