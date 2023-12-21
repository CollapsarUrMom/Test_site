dic = {}

lst = [i.split(', ') for i in iter(input, 'конец')]

for i in lst:
    dic.setdefault(i[0], []).append(int(i[1]))

print(dic)

for i in sorted(dic.keys()):
    res = sum(dic[i])/len(dic[i])
    dic[i] = res

for i in sorted(dic.items(), key= lambda x: (-x[1], x[0])):
    print(i[0], i[1])