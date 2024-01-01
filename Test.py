def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name, mode= 'r', encoding= 'UTF-8') as file:
        count = 0
        lines = [line.strip() for line in file]
        for i in lines:
            if len(i) > 6:
                count += 1
        return count





print(find_lines_len_more_6('hello.txt'))