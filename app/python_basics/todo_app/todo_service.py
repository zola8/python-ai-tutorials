from app.python_basics.todo_app.todo import Todo


class TodoService():
    def __init__(self):
        self.todos = []

    def add_todo(self, *todos: Todo) -> None:
        self.todos.extend(todos)

    def to_string(self) -> str:
        self.todos.sort(key=lambda todo: todo.id)
        return "[]" if not self.todos else "[\n\t" + "\n\t".join(map(str, self.todos)) + "\n]"

    def delete_by_id(self, id: int) -> None:
        self.todos = [todo for todo in self.todos if todo.id != id]

    def find_by_id(self, id: int) -> Todo | None:
        a = [todo for todo in self.todos if todo.id == id]
        return a[0] if a else None


if __name__ == '__main__':
    todo1 = Todo('Go to shop')
    todo2 = Todo('Wash the plates')

    todo_service = TodoService()
    todo_service.add_todo(todo1, todo2)
    print(todo_service.to_string())

    print(todo_service.find_by_id(todo1.id))
    print(todo_service.find_by_id(1))
