from collections import deque

class MyQueue:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        return self.que.popleft()

    def peek(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return len(self.que) == 0


obj = MyQueue()

obj.push(1) # // очередь: [1]
obj.push(2) # // очередь: [1, 2] (крайняя слева — начало очереди)
obj.peek() # // возвращает 1
obj.pop() # // возвращает 1, очередь: [2]
obj.empty() # // возвращает false