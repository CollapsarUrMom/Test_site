def file_n_lines(file_name: str, n: int) -> None:
    file = open(file_name, 'r', encoding= 'UTF-8')
    for i in range(n):
        print(file.readline().strip())
    file.close()


print(file_n_lines('hello.txt', 2))