dic = {}
result = []

for _ in range(int(input())):
    friend, data, month = input().split()
    celendar = dic.setdefault(friend, month)
    #print(celendar)
    
print(dic)
print(dic.values())


for _ in range(int(input())):
    a = input()
    for key in dic:
        if dic[key] == a:
            result.append(key)

print(result)

#keys = [key for key in students if students[key] == target_grade]




