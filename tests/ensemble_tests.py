from Chatguy.handlers.db import *
from Chatguy.handlers.text_generators import generate_words, generate_sentences
from tests.test_api_fuctions import *
from tests.test_config import user_input_word, word_synonym_res
import sys
sys.path.insert(1, '..')



ensemble_tests_dict = {'tests_name': ['test_word_generator_function', 'test_sentence_generator_fuction',
                                      'test_store_corrections', 'test_get_synonyms_word_type', 'test_get_word_equals_suggest_synonyms',
                                      'test_list_suggesting', 'test_join_tuple_string', 'test_phrase_gec', 'test_phrase_aug',
                                      'test_create_model_gec', 'test_create_model'],

                       'tests_input': [user_input_word.texts, user_input_sentence, user_input_corrections.texts,
                                       test_config.word, test_config.word_1, test_config.word_2, user_input_sentence.texts, test_config.string, 'test phrase gec', 'test phrase aug',
                                       'test create model gec', 'test create model'],

                       'tests_output': [test_config.word_synonym_res, test_config.sentence_res,
                                        (test_config.result_corrections_res.id,
                                         test_config.result_corrections_res.source_text,
                                         test_config.result_corrections_res.target_text), test_config.synonyms_teste,
                                        (test_config.synonyms_teste,
                                         test_config.synonyms_caderno), test_config.res_suggested_list,
                                        'phrase_gec', 'aug_list', 'model', 'model']}


for keys in ensemble_tests_dict.keys():
    print('Func keys--> ', keys)

for values in ensemble_tests_dict.values():
    print('\nFunc values --> ', values)
