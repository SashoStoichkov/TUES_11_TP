def accumulate_left(func, a, b):
    result = 0

    for num in b:
        result = func(a, num)
        a = result

    return result

if __name__ == "__main__":

    print(accumulate_left(lambda a, b: a / b, 64, [2, 4, 8]))