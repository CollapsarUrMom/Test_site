def longest_word_in_file(file_name: str) -> str:
    file = open(file_name, mode= 'r', encoding= 'UTF-8')
    count = 0
    sum_numbers = 0
    for word in file.read().split():
        if len(word) == 3:
            count += 1
        elif len(word) == 2:
            sum_numbers += int(word)
    file.close()
    return count, sum_numbers





print(longest_word_in_file('D:\\Alex\\Сегодня\\numbers.txt'))