from fastapi.testclient import TestClient

'''
Testes:

1) Conexão com API
- Rota suggest words
- Rota suggest Sentences
- Rota Store Corrections

OBS: como criar fixture para evitar a repetição de código?
Simular fake_conexion com banco para testar se as funções 
estão funcionando corretamente.

2) Conexão com banco de dados

'''

def test_word_generator(client: TestClient):
    '''
    Teste para garantir conexão com a rota e 
    retornar output corretamente
    '''
    # incluir conexão com banco manualmente para teste
    # Given --> 
    response = client.post(r'/suggest_words/') # When
    assert response.status_code == 200 # Then
    '''assert response.json() == [{
        "word": "pombo",
        "generate": True,
        "entity": False,
        "local": True,
        "suggestions": ["pombo"]
    }]'''

def test_sentence_generator(client: TestClient):
    '''
    Teste para garantir conexão com a rota e 
    retornar output corretamente
    '''
    # incluir conexão com banco manualmente para teste
    # Given -->
    response = client.post(r'/suggest_sentences/') # When
    assert response.status_code == 200 # Then
    '''assert response.json() == {
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
					}
				]
			}]
        }
    }    '''

def test_store_corrections(client: TestClient):
    '''
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    '''
    # incluir conexão com banco manualmente para teste
    # Given --> session = db.create_db(DATABASE_URL)
    response = client.post(r'/store_corrections/') # When
    assert response.status.code == 200 #Then
    # assert db.insert_corrections(session, data[0], data[1])