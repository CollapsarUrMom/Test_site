a = list(map(int, input().split()))

if a == sorted(a, reverse= True) and a[:1] != a[-1:]:
    print(True)
else:
    print(False)