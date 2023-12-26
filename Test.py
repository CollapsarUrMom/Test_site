def create_counter():
    count = 0

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    return increment, decrement


inc_1, dec_1 = create_counter()
print(inc_1())  # увеличиваем на 1
print(inc_1(2))  # увеличиваем на 2
print(inc_1(3))  # увеличиваем на 3
print(dec_1())  # уменьшаем на 1
print(dec_1())  # уменьшаем на 1

print('-' * 15)
print('Создаем новый объект замыкания с другим счетчиком')

inc_2, dec_2 = create_counter()
print(inc_2(10))  # увеличиваем на 10
print(dec_2(5))  # уменьшаем на 5
print(inc_2(100))  # увеличиваем на 100
print(inc_2(50))  # увеличиваем на 50
print(dec_2())  # уменьшаем на 1