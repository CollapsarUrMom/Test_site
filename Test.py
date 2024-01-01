def search_for_unique_words(file_name: str) -> int:
    with open(file_name, mode= 'r', encoding= 'UTF-8') as file:
        res = [i for i in file.read().lower().split()]
        print(len(set(res)))




search_for_unique_words('D:\\Alex\\Сегодня\\lorem.txt')