from fastapi.testclient import TestClient
from app.main import app
from app.user.model_user import User
from app.user.schema_user import User as UserSchema
from app.user.service_user import UserService
from unittest.mock import MagicMock

client = TestClient(app)

user1 = User(id="1", name="John Doe", email="john@example.com", password="secret")
user2 = User(id="2", name="Jane Doe", email="jane@example.com", password="topsecret")

mock_repository = MagicMock()
mock_repository.read.return_value = [user1, user2]
user_service = UserService(repository=mock_repository)


def test_user_service_get():
    users = user_service.get()

    user1_test = UserSchema.model_validate(user1)
    user2_test = UserSchema.model_validate(user2)

    assert users == [user1_test, user2_test]
    mock_repository.read.assert_called_once()
