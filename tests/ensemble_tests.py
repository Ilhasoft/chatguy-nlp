import sys
sys.path.insert(1, '..')
from tests.test_api_fuctions import *
from tests.test_config import user_input_word, word_synonym_res


ensemble_tests_dict = {}
ensemble_tests_dict['Teste']
ensemble_tests_dict['Input']
ensemble_tests_dict['Output']


tests_name = ['test_word_generator_function', 'test_sentence_generator_fuction',
'test_store_corrections', 'test_get_synonyms_word_type', 'test_get_word_equals_suggest_synonyms',
'test_list_suggesting', 'test_join_tuple_string', 'test_phrase_gec', 'test_phrase_aug',
'test_create_model_gec', 'test_create_model' ]

tests_input = [test_word_generator_function(user_input_word.texts),
test_word_generator_function(user_input_word.texts),
test_word_generator_function(user_input_word.texts),
test_word_generator_function(user_input_word.texts),
test_word_generator_function(user_input_word.texts), 
test_word_generator_function(user_input_word.texts),
]

tests_output = [word_synonym_res, word_synonym_res, word_synonym_res,
word_synonym_res, word_synonym_res, word_synonym_res]

for nome in tests_name.items():
    ensemble_tests_dict['Teste'] = tests_name

for input in tests_name.items():
    ensemble_tests_dict['Input'] = tests_input

for output in tests_name.items():
    ensemble_tests_dict['Output'] = tests_output 

