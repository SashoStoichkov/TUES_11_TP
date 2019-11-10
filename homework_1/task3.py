def maxNotes(list_of_parties):
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
    print(leading([[1, 2, 3], [2, 2, 2], [9, 7, 3]]))
