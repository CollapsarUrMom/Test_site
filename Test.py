dic = {}

while input() != 'конец':
    a = input()
    taxi_driver, rating = a.split()
    dic[taxi_driver] = rating
    
print(dic)

