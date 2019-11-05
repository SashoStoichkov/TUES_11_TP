from time import sleep
from math import sqrt


class Iter:
    def __init__(self, number):
        self.__number = number
        self.__numbers = list()

    def __iter__(self):
        if len(self.__numbers) == self.__number + 1:
            return iter(self.__numbers)
        else:
            self.n = 0
            return self

    def __next__(self):
        if self.n <= self.__number:
            self.__numbers.append(self.n)
            self.n += 1

            sleep(1)

            return self.n - 1
        else:
            raise StopIteration


# it = Iter(10)

# for i in it:
#     print(i, end=" ")

# print()

# for i in it:
#     print(i, end=" ")

# print()


def is_prime(n):
    if (n <= 1) or (n % 2 == 0):
        return False
    if (n == 2):
        return True

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True


def generate_prime_numbers():
    number = 1

    while True:
        number += 1

        if is_prime(number):
            yield number


gen = generate_prime_numbers()

for i in gen:
    if i > 100:
        break
    print(i)
