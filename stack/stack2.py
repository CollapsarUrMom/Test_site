from collections import deque



class MyStack:

    def __init__(self):
        self.que = deque()
        

    def push(self, x: int) -> None:
        return self.que.append(x)
    

    def pop(self) -> int:
        for i in range(len(self.que) - 1):
            self.push(self.que.popleft())
        return self.que.popleft()


    def top(self) -> int:
        return self.que[-1]


    def empty(self) -> bool:
        return len(self.que) == 0



stack = MyStack()
stack.push(1)
stack.push(2)
stack.top() # // возвращает 2
stack.pop() # // возвращает 2
stack.empty() # // возвращает False


# [null, null, null, 2, 2, false]