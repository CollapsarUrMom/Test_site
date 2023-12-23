import math
rad = 0.01745329252 # Радианы

start = 1 # Градусы
step = 3 # Шаг
end = 365 # Конечный градус
diametr = 290 # Диаметр

for i in range(start, end, step):
    x = (diametr / 2) * math.cos(rad * i)
    y = (diametr / 2) * math.sin(rad * i)
    x_next = (diametr / 2) * math.cos(rad * (i + step))
    y_next = (diametr / 2) * math.sin(rad * (i + step))
    processing_width = math.sqrt(((x - x_next) ** 2) + ((y - y_next) ** 2))
    print(f'x {x} y {y} при {i} градусах')
    print(f'Максимальная ширина съёма {processing_width}')
    print()