import sys
sys.path.insert(1, '..')

from tests.test_config import user_input_word, word_synonym_res
from tests.test_api_fuctions import *
from Chatguy.handlers.text_generators import generate_words, generate_sentences
from Chatguy.handlers.db import *

word = 'teste'
word_1 = 'teste'
word_2 = 'caderno'
string = ('teste', 'teste', 'teste')


ensemble_tests_dict = {'tests_name': ['test_word_generator_function', 'test_sentence_generator_fuction',
        'test_store_corrections', 'test_get_synonyms_word_type', 'test_get_word_equals_suggest_synonyms',                              
        'test_list_suggesting', 'test_join_tuple_string', 'test_phrase_gec', 'test_phrase_aug',                              
        'test_create_model_gec', 'test_create_model'], 
                                      
                        'tests_input': [user_input_word.texts, user_input_sentence, user_input_corrections.texts,
word, word_1, word_2, user_input_sentence.texts, string, 'test phrase gec', 'test phrase aug',
'test create model gec', 'test create model' ],

                        'tests_output': [test_config.word_synonym_res, test_config.sentence_res,
(test_config.result_corrections_res.id,
test_config.result_corrections_res.source_text,
test_config.result_corrections_res.target_text), test_config.synonyms_teste,
(test_config.synonyms_teste, test_config.synonyms_caderno), test_config.res_suggested_list,
 'phrase_gec','aug_list', 'model', 'model']}                                                             
                                                                                                                     
print('Func keys--> ', ensemble_tests_dict.keys())
print('\nFunc values --> ', ensemble_tests_dict.values())
print('\nFunc name --> ', ensemble_tests_dict['tests_name'])
print('\nFunc input --> ', ensemble_tests_dict['tests_input'])
print('\nFunc output --> ', ensemble_tests_dict['tests_output'])




