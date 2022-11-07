from typing import Callable
import pytest
import sys
import os
import time
import statistics
import functools 
from datetime import datetime
sys.path.insert(1, '..')

import time
from typing import Callable
from fastapi.testclient import TestClient
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute

'''
Fixtures 
--------

Fixture connection to Database
@pytest.fixture(scope = 'function')
def setup_database():
	session = db.create_db(DATABASE_URL)
	session.close()


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


def timer(func):
    '''print the runtime of the decorated function'''
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        run_time = end_time - start_time
        print_string_timer = (f'Finished {func.__name__!r} in {run_time:.4} seconds')

        print('\n', print_string_timer)

        
        return result
    return timer_wrapper    


class StoreCorrections:
    def __init__(self):
        self.id = 1
        self.source_text = 'olá tudo bem como você vai?1'
        self.target_text = 'tchau, to vazando, saindo fora meu chegado, até mais!1'



class TimedRoute(APIRoute):
    def get_route_(self) -> Callable:
        original_route = super().get_route()
        def custom_route(request: Request) -> Response:
            before = time.perf_counter()
            response: Response = original_route(request)
            duration = time.perf_counter() - before

            print(f'route duration: {duration}')
            print(f'route duration: {duration:.4}')
            print(f'route response: {response}')
            print(f'route response header: {response.headers}')

        return custom_route
    '''
        self.tempo_inicial = time.perf_counter()
        self.tempo_rodando = func(*args, **kwargs)
        self.tempo_final = time.perf_counter()
        self.tempo_total = time.perf_counter() - self.tempo_incial
        print_string_timer = (f'Finished {func.__name__!r} in {run_time:.4} seconds')
    '''
    
            

        
            
        
        
        
 
router = FastAPI()

client = TestClient(router)

routes = [router.post(r'/suggest_words/'),
            router.post(r'/suggest_sentences/'),
            router.post(r'/suggest_sentences/'),
            router.post(r'/recover_sentences/'),
            router.post(r'/store_corrections/'),
            ]

@timer
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
