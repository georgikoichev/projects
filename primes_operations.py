from math import sqrt, floor
from projects.validation import is_int, is_list


def all_primes(n):
    is_int(n)
    primes = [0] * (n+1)
    result = []

    for i in range(2, floor(sqrt(n)) + 1):
        for j in range(i * i, n + 1, i):
            primes[j] = 1

    for i in range(2, len(primes)):
        if primes[i] == 0:
            result.append(i)

    return result


def is_prime(n):
    is_int(n)
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0 and n != i:
            return False
    return True


def selected_primes(numbers):
    is_list(numbers)
    result = []

    for n in numbers:
        if is_prime(n):
            result.append(n)

    return result