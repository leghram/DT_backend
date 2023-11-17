from fastapi.testclient import TestClient
from app.main import app
from app.user.model_user import User
from app.user.repository_user import UserRepository
from unittest.mock import MagicMock
import pytest


client = TestClient(app)


def test_get_users_validate_route():
    response = client.get("/apiv1/users")
    assert response.status_code == 200


@pytest.fixture
def mock_session():
    return MagicMock()


def test_read_users(mock_session):
    user_repo = UserRepository(session=mock_session)

    user1 = User(id=1, name="User1 Uno")
    user2 = User(id=2, name="User2 Dos")

    mock_session.query.return_value.all.return_value = [user1, user2]
    users = user_repo.read()

    assert users == [user1, user2]
    mock_session.query.assert_called_once_with(User)
    mock_session.query.return_value.all.assert_called_once()
