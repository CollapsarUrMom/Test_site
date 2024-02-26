# Напишите определение класса Stack
class Stack:

    def __init__(self, values= []):
        self.values = list(values)

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values == []:
            print('Empty Stack')
        self.values.[-1]

    def peek(self):
        if self.values == []:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]
        
    def is_empty(self):
        if self.values == []:
            return True
        return False
    
    def size(self):
        return len(self.values)

# Ниже код для проверки класса Stack

s = Stack()
assert s.values == []
assert isinstance(s, Stack)

s.peek()  # распечатает 'Empty Stack'
assert s.is_empty() is True
s.push('cat')
assert s.size() == 1
assert s.peek() == 'cat'

s.push('dog')
assert s.size() == 2
assert s.peek() == 'dog'

s.push(True)
assert s.size() == 3
assert s.is_empty() is False

s.push(777)
assert s.size() == 4

assert s.pop() == 777
assert s.size() == 3

assert s.pop() is True
assert s.size() == 2

s.push(123)
s.push(123456)
assert s.peek() == 123456
assert s.size() == 4

assert s.pop() == 123456
assert s.pop() == 123
assert s.pop() == 'dog'
assert s.is_empty() is False
assert s.pop() == 'cat'
assert s.is_empty() is True


d = Stack()
assert d.peek() is None  # Печатает "Empty Stack"
assert d.pop() is None  # Печатает "Empty Stack"
d.push('hello')
assert d.size() == 1
d.push('world')
assert d.size() == 2
assert d.peek() == 'world'
assert d.pop() == 'world'
assert d.peek() == 'hello'