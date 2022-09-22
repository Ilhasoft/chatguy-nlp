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


'''

def test_get_root(client: TestClient) -> None:
    response = client.get('/')
    body = response.json()
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Deu certo!"}



def test_word_generator(client: TestClient) -> None:
    '''
    Teste para garantir conexão com a rota e 
    retornar output corretamente
    '''
    # incluir conexão com banco manualmente para teste
    response = client.post(r'/suggest_words/') # Given
    body = response.json() # When
    assert response.status_code == 200 # Then



def test_sentence_generator(client: TestClient):
    '''
    Teste para garantir conexão com a rota e 
    retornar output corretamente
    '''
    response = client.post(r'/suggest_sentences/') # Given 
    body = response.json() # When
    assert response.status_code == 200 # Then
    


'''
--------------------------
2) Conexão com banco de dados

def test_store_corrections(client: TestClient):
    
    Teste para garantir conexão com a rota, conexão com banco
    e retornar output corretamente
    
    # incluir conexão com banco manualmente para teste
    # session = db.create_db(DATABASE_URL_TEST) #Given 
    response = client.post(r'/store_corrections/') # When
    assert response.status.code == 200 #Then
    # assert db.insert_corrections(session, data[0], data[1])

'''

    