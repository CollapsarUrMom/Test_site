dic = {}

lst = [i.split(', ') for i in iter(input, 'конец')]

for i in lst:
    dic.setdefault(i[0], []).append(int(i[1]))

for i in sorted(dic.keys()):
    res = sum(dic[i])/len(dic[i])
    dic[i] = res

    
my_lst = sorted(subject_marks, key = lambda valuation: valuation[0][0])

[print(*i) for i in sorted(my_lst, key = lambda valuation: valuation[1], reverse = True)]


[print(i[0], i[1]) for i in sorted(dic.items(), key= lambda x: (x[1], x[0]))]