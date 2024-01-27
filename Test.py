def find_keys(*args, **kwargs):
    for i in kwargs.items():
        print(type(i[1]))
        if isinstance(i[1], list):
            print(i[0])

assert find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) == ['A', 'b', 't', 'W']
assert find_keys(name='Bruce', surname='Wayne') == []
assert find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) == ['Also', 'marks']