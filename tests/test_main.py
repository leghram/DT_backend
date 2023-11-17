from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/apiv1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Api Service"}
