def group_by_f(func, lst):
    result = dict()

    for el in lst:
        result_key = func(el)

        if result_key not in result.keys():
            result[result_key] = list()
            result[result_key].append(el)
        else:
            result[result_key].append(el)

    return result


if __name__ == "__main__":
    d1 = group_by_f(lambda a: a % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    d2 = group_by_f(len, [[1], [7, 8], [1, 2, 3, 4], [4], ["random", "words"]])

    print(d1)
    print(d2)
