#lst = []
#string = input()
#for i in string.split():
    #a = i.upper()
    #b = i.lower()
    #c = a, b
    #lst.append(c)
#print(lst)

#==================================

#lst = []

#def handler(word):
    #upper = word.upper()
    #lower = word.lower()
    #return upper, lower

#for letter in map(handler, input().split()):
    #lst.append(letter)
#print(lst)

#===================================

print(list(map(lambda x:(x.upper(), x.lower()), input().split())))