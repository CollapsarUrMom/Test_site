def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
r = counter()
print(q())
q()
print(q())
print(r())