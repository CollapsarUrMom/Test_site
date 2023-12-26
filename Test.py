#def add(a, b):
    #return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args,**kwargs)

    return inner
q = counter(lambda a, b: a + b)

q(10, 20)
q(2,5)