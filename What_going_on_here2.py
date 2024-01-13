from typing import Generator

def my_range_gen(*args) -> Generator[int, None, None]:
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
        if stop < 0:
            exit()
    elif len(args) == 2:
        start, stop = args
        step = 1
        if start > stop or start == stop:
            exit()
    elif len(args) == 3:
        start, stop, step = args
        if step == 0 or step < 0 and start < stop or start > stop or start == stop:
            exit()

    while start != stop:
        yield start
        start += step

tests = [(5,), (10,), (-3,), (-5, 10), (10, 3), (30, 300, 1), (0, -10, -2), (0, -10, 5), (10, 10), (10, 10, 10)< (0, 0, 0), (20, 10, 3), (1, 10, -2), (4, 8, 2), (8, 5, -1), (100, 300, 13), (10, 30, 3), (4, 8, 0)]
for i in tests:
    assert [j for j in range(*i)] == [t for t in my_range_gen(*i)]