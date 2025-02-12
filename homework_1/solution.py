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


def has_same_ingredients(medicine1, medicine2):

    medicine1[1].sort()
    medicine2[1].sort()

    if len(medicine1[1]) <= len(medicine2[1]):
        for i in range(len(medicine1[1])):
            if medicine2[1][i][0] != medicine1[1][i][0]:
                return False
        return True
    else:
        return False


def is_stronger(medicine1, medicine2):
    sum_of_divs = 0

    if has_same_ingredients(medicine2, medicine1):
        for i in range(len(medicine2[1])):
            sum_of_divs += medicine1[1][i][1] - medicine2[1][i][1]

        if sum_of_divs > 0:
            return True
        else:
            return False

    else:
        return False


def least_stronger(medicine, lst_of_meds):
    sums = dict()

    for ind in range(len(lst_of_meds)):
        sum_of_divs = 0
        med = lst_of_meds[ind]

        if has_same_ingredients(medicine, med) and is_stronger(med, medicine):
            for i in range(len(medicine[1])):
                sum_of_divs += med[1][i][1] - medicine[1][i][1]

            sums[ind] = sum_of_divs

    if sums == {}:
        return []
    else:
        minimum_difference = min(sums.values())

        for k, v in sums.items():
            if v == minimum_difference:
                index = k

        return lst_of_meds[k]


def strong_relation(list_of_medicines):
    result = list()

    for medicine in list_of_medicines:
        stronger_medicines = list()

        for med in list_of_medicines:
            if is_stronger(med, medicine) is True:
                stronger_medicines.append(med[0])

        result.append((medicine, stronger_medicines))

    return result


def max_notes(list_of_parties):
    max_sum = 0

    for party in list_of_parties:
        if sum(party) > max_sum:
            max_sum = sum(party)

    return max_sum


def leading(list_of_parties):
    result_list = list()

    for i in range(len(list_of_parties)):
        result_list.append([0]*len(list_of_parties[i]))

    parties = dict()

    for ind in range(len(list_of_parties)):
        for i in range(len(list_of_parties)):
            parties[i] = list_of_parties[i][ind]

        max_note = 0

        for k, v in parties.items():
            if v > max_note:
                max_note = v

        for k, v in parties.items():
            if v == max_note:
                result_list[k][ind] = 1

    result_sum_list = list()

    for lst in result_list:
        result_sum_list.append(sum(lst))

    max_sum = max(result_sum_list)

    for i in range(len(result_sum_list)):
        if result_sum_list[i] == max_sum:
            return i


if __name__ == "__main__":
    pass
