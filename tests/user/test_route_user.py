from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock, patch

client = TestClient(app)


def test_get_users_validate_route():
    mock_service = MagicMock()
    mock_user1 = MagicMock()
    mock_user2 = MagicMock()
    mock_user1.configure_mock(id="1", name="John Doe", email="john@example.com", password="secret")
    mock_user2.configure_mock(
        id="2", name="Jane Doe", email="jane@example.com", password="topsecret"
    )
    mock_service.get.return_value = [mock_user1, mock_user2]

    with patch("app.user.route_user.user_service", mock_service):
        response = client.get("/apiv1/users/")

    assert response.status_code == 200
