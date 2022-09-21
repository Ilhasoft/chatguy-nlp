from fastapi import FastAPI
from fastapi.testclient import TestClient

def test_get_route(client: TestClient):
    response = client.get('/test')
    assert response.status_code == 200
    assert response.json() =={"mensagem": "Deu certo!"}

