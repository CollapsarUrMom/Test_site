dic = {}

for _ in range(int(input())):
    friend, data, month = input().split()
    celendar = dic.setdefault(friend, [month, data])
    print(celendar)
    
print(dic)


for _ in range(int(input())):
    input()