def accumulate_right(func, a, b):
    result = 0
    b = reversed(b)

    for num in b:
        result = func(num, a)
        a = result

    return result

if __name__ == "__main__":

    print(accumulate_right(lambda a, b: a / b, 8, [16, 32, 64]))