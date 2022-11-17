from typing import Callable
import pytest
import sys
import os
import time
import statistics
import functools 
from datetime import datetime
import tracemalloc
from time import perf_counter 
sys.path.insert(1, '..')
sys.path.insert(1, '.')
from typing import Generator
import time
from typing import Callable
from fastapi.testclient import TestClient
from fastapi import FastAPI


'''
Fixtures 
--------
Fixture connection to Database
@pytest.fixture(scope = 'function')
def setup_database():
	session = db.create_db(DATABASE_URL)
	session.close()

router = FastAPI()

@pytest.fixture(scope='function')
def client() -> Generator:
    with TestClient(router):
        yield TestClient


Decorators
----------
'''

def log_datetime(func):
    '''
    Decorator to register log
    '''
    def wrapper():
        print_string_datetime = (f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%d-%m-%Y %H:%M:%S")}')
        print(f'{"-"*len(print_string_datetime)}')
        print(print_string_datetime)
        print(f'{"-"*len(print_string_datetime)}')
        func()
    return wrapper   


def measure_performance(func):
    '''Measure performance of a function'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


class StoreCorrections:
    def __init__(self):
        self.id = 1
        self.source_text = 'olá tudo bem como você vai?1'
        self.target_text = 'tchau, to vazando, saindo fora meu chegado, até mais!1'

'''
class MeasurePerformance:
    def __init__(self, func):
        self.func = func
    def _call__(self, func, *args, **kwargs):
        tracemalloc.start()
        self.start_time = perf_counter()
        self.func = func(*args, **kwargs)
        self.current, self.peak = tracemalloc.get_traced_memory()
        self.finish_time = perf_counter()
        self.message = (f'Function: {self.func.__name__}',
                        f'\nMethod: {self.func.__doc__}',
                        f'\nMemory usage:\t\t {self.current / 10**6:.6f} MB \n'
                        f'\nPeak memory usage:\t {self.peak / 10**6:.6f} MB ',
                        f'\nTime elapsed is seconds: {self.finish_time - self.start_time:.6f}',
                        f'{"-"*40}' )
        tracemalloc.stop()
    def showPerformance(self):
        print(self.message)
'''

router = FastAPI()

routes = [router.post(r'/suggest_words/'),
            router.post(r'/suggest_sentences/'),
            router.post(r'/suggest_sentences/'),
            router.post(r'/recover_sentences/'),
            router.post(r'/store_corrections/'),
            ]


def application_route(route):
    for route in routes:
        return route



word = 'teste'

word_1 = 'teste'

word_2 = 'caderno'

string = ('teste', 'teste', 'teste')

list_phrases = ['teste']

input_test = 'ping'

user_input_word = {
    "texts": [{
        "word": "mulher",
        "generate": True,
        "entity": False,
        "local": True
    }, {
        "word": "sapato",
        "generate": True,
        "entity": False,
        "local": False
    }, {
        "word": "compra",
        "generate": True,
        "entity": True,
        "local": False
    }, {
        "word": "no",
        "generate": False,
        "entity": False,
        "local": False
    }, {
        "word": "vender",
        "generate": True,
        "entity": False,
        "local": True
    }]
}

word_synonym_res = [
    {
        "word": "mulher",
        "generate": True,
                "entity": False,
                "local": True,
                "suggestions": [
                    "mulher",
                    "fêmea",
                    "senhora",
                    "dona",
                    "adulta",
                    "maior",
                    "moça",
                    "mocinha",
                    "esposa",
                    "cônjuge",
                    "consorte",
                    "patroa",
                    "dama",
                    "madame",
                    "companheira",
                    "namorada",
                    "caso",
                    "amante"
                ]
    },
    {
        "word": "sapato",
        "generate": True,
                "entity": False,
                "local": False,
                "suggestions": [
                    "sapato",
                    "calçado"
                ]
    },
    {
        "word": "compra",
        "generate": True,
                "entity": True,
                "local": False,
                "suggestions": [
                    "compra",
                    "merca",
                    "obtenção",
                    "aquisição",
                    "artigo",
                    "mercadoria",
                    "produto",
                    "mercancia",
                    "corrupção",
                    "peita",
                    "suborno"
                ]
    },
    {
        "word": "no",
        "generate": False,
                "entity": False,
                "local": False,
                "suggestions": [
                    "no"
                ]
    },
    {
        "word": "vender",
        "generate": True,
                "entity": False,
                "local": True,
                "suggestions": [
                    "vender",
                    "alienar",
                    "ceder",
                    "transferir",
                    "comercializar",
                    "comerciar",
                    "mercadejar",
                    "mercanciar",
                    "mercantilizar",
                    "mercar",
                    "negociar",
                    "transacionar",
                    "delatar",
                    "acusar",
                    "denunciar",
                    "entregar",
                    "malsinar",
                    "sacrificar",
                    "trair",
                    "esbanjar",
                    "exibir",
                    "ostentar",
                    "ter",
                    "corromper-se",
                    "prostituir-se"
                ]
    }
]


user_input_sentence = {"isquestion": True,
                       "intent": "teste",
                       "texts": [
                           {
                               "word": "existem",
                               "generate": True,
                               "entity": "existir",
                               "suggestions": [
                                   "há",
                                   "existem"
                               ]
                           },
                           {
                               "word": "muitas",
                               "generate": True,
                               "entity": False,
                               "suggestions": [
                                   "diversas"
                               ]
                           },
                           {
                               "word": "pessoas",
                               "generate": True,
                               "entity": "sujeito",
                               "suggestions": [
                                   "homens",
                                   "mulheres",
                                   "crianças"
                               ]
                           },
                           {
                               "word": "no",
                               "generate": False,
                               "entity": False,
                               "suggestions": ["no"]
                           },
                           {
                               "word": "mundo",
                               "generate": True,
                               "entity": False,
                               "suggestions": [
                                   "planeta"
                               ]
                           }
                       ]
                       }

sentence_res = {
	"rasa_nlu_data": {
		"regex_features": [],
		"entity_synonyms": [],
		"common_examples": [
			{
				"text": "há diversas homens no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 2,
						"value": "há",
						"entity": "existir"
					},
					{
						"start": 12,
						"end": 18,
						"value": "homens",
						"entity": "sujeito"
					}
				]
			},
			{
				"text": "há diversas mulheres no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 2,
						"value": "há",
						"entity": "existir"
					},
					{
						"start": 12,
						"end": 20,
						"value": "mulheres",
						"entity": "sujeito"
					}
				]
			},
			{
				"text": "há diversas crianças no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 2,
						"value": "há",
						"entity": "existir"
					},
					{
						"start": 12,
						"end": 20,
						"value": "crianças",
						"entity": "sujeito"
					}
				]
			},
			{
				"text": "existem diversas homens no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 7,
						"value": "existem",
						"entity": "existir"
					},
					{
						"start": 17,
						"end": 23,
						"value": "homens",
						"entity": "sujeito"
					}
				]
			},
			{
				"text": "existem diversas mulheres no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 7,
						"value": "existem",
						"entity": "existir"
					},
					{
						"start": 17,
						"end": 25,
						"value": "mulheres",
						"entity": "sujeito"
					}
				]
			},
			{
				"text": "existem diversas crianças no planeta ?",
				"intent": "teste",
				"entities": [
					{
						"start": 0,
						"end": 7,
						"value": "existem",
						"entity": "existir"
					},
					{
						"start": 17,
						"end": 25,
						"value": "crianças",
						"entity": "sujeito"
					}
				]
			}
		]
	}
}

user_input_corrections = {
    "texts": [["olá tudo bem como você vai?1"],
              ["tchau, to vazando, saindo fora meu chegado, até mais!1"]]
}

result_corrections_res = StoreCorrections()

synonyms_teste = ['avaliação', 'exame', 'prova',
                  'provação', 'verificação', 'constatação', 'ensaio',
                  'experiência', 'experimentação', 'experimento',
                  'investida', 'tentativa', 'mostragem']

synonyms_caderno = ['caderneta', 'livrete', 'seção',
                    'suplemento', 'brochura', 'fascículo', 'folheto',
                    'livro', 'bloco', 'agenda']

res_suggested_list = ['há diversas homens no planeta', 'há diversas mulheres no planeta',
'há diversas crianças no planeta', 'existem diversas homens no planeta',
'existem diversas mulheres no planeta', 'existem diversas crianças no planeta']