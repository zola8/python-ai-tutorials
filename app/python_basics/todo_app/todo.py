import random
from enum import Enum

class TodoStatus(Enum):
    IN_PROGRESS = 1
    DONE = 2
    CANCELLED = 3

# functional syntax
# TodoStatus = Enum('TodoStatus', [('IN_PROGRESS', 1), ('DONE', 2), ('CANCELLED', 3)])



class Todo():
    def __init__(self, text, status=TodoStatus.IN_PROGRESS):
        self.id = random.randint(1000, 9999)
        self.text = text
        self.status = status

    def __str__(self):
        return f"[{self.id}] [{self.status.name}] {self.text}"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    todo = Todo('Go to shop')
    print(todo)
