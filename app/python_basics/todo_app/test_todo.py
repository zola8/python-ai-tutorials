from app.python_basics.todo_app.todo import Todo, TodoStatus

todo = Todo('Go to shop')


def test_todo_creation():
    assert todo.status == TodoStatus.IN_PROGRESS
    assert todo.text == 'Go to shop'
    assert 1000 <= todo.id <= 9999


def test_todo_str():
    number = todo.__str__()[1:5]
    assert int(number), "compilation should be done, no exception should be raised"
