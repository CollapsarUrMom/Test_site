def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)

    return inner

r1 = average_numbers()
print(r1(1))
print(r1(10))
print(r1(100))
print(r1(1000))
print(r1(10000))

r2 = average_numbers()
print(r2(1))
print(r2(10))
print(r2(100))
print(r1(100000))