from operator import gt, lt

def my_range_gen(*args):
    start, stop, step = 0, 0, 1
    match len(args):
        case 1:
            stop = args[0]
        case 2:
            start, stop = args
        case 3:
            start, stop, step = args
        case _:
            exit()
    condition = lt if step > 0 else gt if step < 0 else lambda a, b: False
    while condition(start, stop):
        yield start
        start += step