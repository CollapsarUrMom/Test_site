def create_accumulator():
    value = 0
    def inner_func(num):
        nonlocal value
        value += num
        return value
    return inner_func

simulator_1 = create_accumulator()
print(simulator_1(2))
print(simulator_1(5))
print(simulator_1(10))

simulator_2 = create_accumulator()
print(simulator_2(11))
print(simulator_2(10))
print(simulator_2(15))

print(simulator_1(3))