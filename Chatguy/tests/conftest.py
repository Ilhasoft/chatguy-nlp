from fastapi.testclient import TestClient
from email.generator import Generator
import pytest
from app import router


@pytest.fixture(scope='function')
def client() -> Generator:
    with TestClient(router) as c:
        yield c

