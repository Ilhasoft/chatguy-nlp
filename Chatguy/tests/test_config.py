from fastapi.testclient import TestClient
from email.generator import Generator
import app
import pytest 

@pytest.fixture(scope='function')
def client() -> Generator:
    with TestClient(app) as c:
        yield c
