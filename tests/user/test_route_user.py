from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_users_validate_route():
    response = client.get("/apiv1/users")
    assert response.status_code == 200
