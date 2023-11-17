from unittest.mock import MagicMock
import pytest
from app.user.repository_user import UserRepository
from app.user.model_user import User


@pytest.fixture
def mock_session():
    return MagicMock()


def test_user_repository_read(mock_session):
    user_repo = UserRepository(session=mock_session)

    user1 = User(id=1, name="John Doe")
    user2 = User(id=2, name="Jane Doe")

    mock_session.query.return_value.all.return_value = [user1, user2]

    users = user_repo.read()

    assert users == [user1, user2]
    mock_session.query.assert_called_once_with(User)
    mock_session.query.return_value.all.assert_called_once()
