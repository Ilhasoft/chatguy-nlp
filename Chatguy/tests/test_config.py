import pytest
from app import DATABASE_URL, router
from app import router

'''
@pytest.fixture(scope = 'function')
def setup_database():
	session = db.create_db(DATABASE_URL)
	session.close()'''

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


user_input_sentence = {
    "isquestion": True,
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
                    }
                ]
            }
        ]
    }
}, {
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
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
                        "entity": "brilhar"
                    }
                ]
            }
        ]
    }
}

user_input_corrections = {
    "texts": [["olá tudo bem como você vai?1",
	 "olá tudo bem como você vai?2",
	 "olá tudo bem como você vai?3"],
	["tchau, to vazando, saindo fora meu chegado, até mais!1",
	"tchau, to vazando, saindo fora meu chegado, até mais!2",
	"tchau, to vazando, saindo fora meu chegado, até mais!3"]]
}

result_corrections_res = {
	"200": "Inserted!"
}

synonyms_teste = ['avaliação', 'exame', 'prova',
                  'provação', 'verificação', 'constatação', 'ensaio',
                  'experiência', 'experimentação', 'experimento',
                  'investida', 'tentativa', 'mostragem']

synonyms_caderno = ['caderneta', 'livrete', 'seção',
                    'suplemento', 'brochura', 'fascículo', 'folheto',
                    'livro', 'bloco', 'agenda']
