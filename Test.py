weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = ((i, weekday[(i + 4) % 7]) for i in range(1, 78))

for i in days:
    print(i)