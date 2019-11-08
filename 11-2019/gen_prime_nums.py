from math import sqrt


def is_prime(n):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2:
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
