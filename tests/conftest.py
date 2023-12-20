import pytest
from fastapi.testclient import TestClient

from source.app import app


@pytest.fixture
def client():
    return TestClient(app)
