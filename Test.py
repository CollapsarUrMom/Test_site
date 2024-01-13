from typing import Generator

def my_range_gen(num) -> Generator[int, None, None]:
    start = 0
    end = num - 1
    while start != end:
        start += 1
        yield start

for i in my_range_gen(10):
    print(i)