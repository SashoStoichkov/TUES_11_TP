def has_same_ingredients(medicine1, medicine2):

    medicine1[1].sort()
    medicine2[1].sort()

    if len(medicine2[1]) <= len(medicine1[1]):
        for i in range(len(medicine2[1])):
            if medicine1[1][i][0] != medicine2[1][i][0]:
                return False
        return True
    else:
        return False


def isStronger(medicine1, medicine2):
    sum_of_divs = 0

    if has_same_ingredients(medicine1, medicine2):
        for i in range(len(medicine2[1])):
            sum_of_divs += medicine1[1][i][1] - medicine2[1][i][1]

        if sum_of_divs > 0:
            return True
        else:
            return False

    else:
        return False


def leastStronger(medicine, list_of_medicines):
    for med in list_of_medicines:
        if isStronger(med, medicine):
            return med

    return []


def strongRelation(list_of_medicines):
    result = list()

    for medicine in list_of_medicines:
        stronger_medicines = list()

        for med in list_of_medicines:
            if isStronger(med, medicine) is True:
                stronger_medicines.append(med[0])

        result.append((medicine, stronger_medicines))

    return result


if __name__ == "__main__":
    A = ("A", [("p", 5), ("q", 3)])
    B = ("B", [("p", 4), ("q", 3)])
    C = ("C", [("p", 3)])
    D = ("D", [("p", 4.5), ("q", 3), ("r", 1)])

    # print(has_same_ingredients(A, B))
    # print(isStronger(C, A))

    # print(leastStronger(A, [B, C, D]))

    list_of_medicines = [A, B, C]
    print(strongRelation(list_of_medicines))
