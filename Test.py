def create_file_with_numbers(n: int) -> None:
    file = open(f'range_{n}.txt', mode= 'w')
    for num in range(1, n + 1):
        file.write(str(num) + '\n')
    file.close()

print(create_file_with_numbers(6))