from app.python_basics.todo_app.todo import Todo
from app.python_basics.todo_app.todo_service import TodoService

todo1 = Todo('Go to shop')
todo1.id = 1009
todo2 = Todo('Wash the plates')
todo2.id = 1008


def test_add_one_todo():
    todo_service = TodoService()
    todo_service.add_todo(todo1)
    assert len(todo_service.todos) == 1
    assert todo_service.todos[0].id == todo1.id


def test_add_multiple_todos():
    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    assert len(todo_service.todos) == 2


def test_todos_are_sorted_to_string():
    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    todo_service.to_string()
    assert todo_service.todos[0].id < todo_service.todos[1].id


def test_delete_by_id():
    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    todo_service.delete_by_id(todo1.id)
    assert len(todo_service.todos) == 1
    assert todo_service.todos[0].id == todo2.id


def test_delete_by_id_not_found():
    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    todo_service.delete_by_id(123)
    assert len(todo_service.todos) == 2


def test_find_by_id():
    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    assert todo_service.find_by_id(todo1.id)


def test_find_by_id_not_exist():
    todo_service = TodoService()
    assert todo_service.find_by_id(1) is None
