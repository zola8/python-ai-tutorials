import random

import pytest

from app.python_basics.todo_app.todo import Todo, TodoStatus


def test_todo_creation():
    todo = Todo('Go to shop')
    assert todo.status == TodoStatus.IN_PROGRESS
    assert todo.text == 'Go to shop'
    assert 1000 <= todo.id <= 9999


@pytest.fixture
def mock_random_id(monkeypatch):
    """Fixture that mocks random.randint to return a consistent ID"""

    def _mock_random_id(mock_value=9999):
        monkeypatch.setattr(random, 'randint', lambda a, b: mock_value)
        return mock_value

    return _mock_random_id


def test_todo_with_fixture(mock_random_id):
    expected_id = mock_random_id(1234)
    todo = Todo("Test with fixture")
    assert todo.id == expected_id


def test_todo_str(mock_random_id):
    expected_id = mock_random_id(1234)
    todo = Todo('Go to shop')
    number = todo.__str__()[1:5]
    assert int(number) == expected_id, "compilation should be done, no exception should be raised"
