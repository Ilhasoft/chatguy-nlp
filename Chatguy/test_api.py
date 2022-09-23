import pytest
from handlers import db, text_generators
from types import SimpleNamespace
import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
adapter = os.environ['POSTGRES_ADAPTER']

DATABASE_URL = f'{adapter}://{user}:{password}@{host}:{port}'


userInput = {
"texts" : [{
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

bg_res = [
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

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

userInput = dotdict(userInput)


#userInput = json.dumps(userInput)
#userInput = json.loads(userInput, object_hook=lambda d: SimpleNamespace(**d))

def test_connection():
    print('hi')
    print(userInput.texts)
    session = db.create_db(DATABASE_URL)
    keys = userInput.texts
    result = text_generators.generate_words(keys, session)
    session.close()
    assert result == bg_res
    #session = db.create_db(DATABASE_URL)
    #keys = userInput.texts
    #assert text_generators.generate_words(keys, session) == 5
