def maxNotes(list_of_parties):
    max_sum = 0

    for party in list_of_parties:
        if sum(party) > max_sum:
            max_sum = sum(party)

    return max_sum


def leading(list_of_parties):
    parties = dict()

    index = len(list_of_parties) - 1

    for i in range(len(list_of_parties)):
        parties[i] = list_of_parties[i][index]

    max_note = 0

    for k, v in parties.items():
        if v > max_note:
            max_note = v

    for k, v in parties.items():
        if v == max_note:
            return k


if __name__ == "__main__":
    print(leading([[1, 2, 3], [2, 2, 2], [9, 7, 3]]))
