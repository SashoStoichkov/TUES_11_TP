def accumulate_left(func, a, b):
    return float(accumulate_left(func, func(a, b[0]), b[1:])) if b else a

def accumulate_right(func, a, b):
    return float(accumulate_right(func, func(b[-1], a), b[:-1])) if b else a

if __name__ == "__main__":

    print(accumulate_left(lambda a, b: a / b, 64, [2, 4, 8]))
    print(accumulate_right(lambda a, b: a / b, 8, [16, 32, 64]))

    print(accumulate_left(lambda a, b: a + b, 64, list(range(1, 501))))
