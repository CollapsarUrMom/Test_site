with open('D:\\Alex\\Сегодня\\words.txt', mode= 'r', encoding= 'UTF-8') as file:
    res = [i for i in file.read().upper().split()]
    for word in sorted(set(res), key= lambda x: (len(x), x)):
        if word[-2:] == 'ЕЯ':
            print(word)     