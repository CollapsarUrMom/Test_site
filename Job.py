import math

rad = 0.01745329252
sag = 3

for i in range(3, 365, 3):
    x = (290 / 2) * math.cos(rad * i)
    y = (290 / 2) * math.sin(rad * i)
    x_next = (290 / 2) * math.cos(rad * (i + sag))
    y_next = (290 / 2) * math.sin(rad * (i + sag))
    l_x = x - x_next
    l_y = y - y_next
    processing_width = math.sqrt((l_x ** 2) + (l_y ** 2))
    print(f'x {x} y {y} при {i} градусах')
    print(f'Максимальная ширина съёма {processing_width}')
    print()