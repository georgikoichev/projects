from projects.primes_operations import is_prime, all_primes
from projects.validation import is_int


def factors(n):
    is_int(n)
    if is_prime(n):
        return [n]

    result = []
    primes = all_primes(n)

    for i in primes:
        while n % i == 0:
            n /= i
            result.append(i)

        if n == 1:
            break
    return result


def common_factors(n1, n2):
    is_int(n1)
    is_int(n2)
    first_factors = factors(n1)
    second_factors = factors(n2)
    result = []

    for i in first_factors:
        if i in second_factors:
            result.append(i)
    return result


def common_denominator(n1, n2):
    is_int(n1)
    is_int(n2)
    if n1 == n2:
        return n1

    diff = n1 % n2
    while diff != 0:
        n1 = n2
        n2 = diff
        diff = n1 % n2
    return n2


def common_multiple(n1, n2):
    is_int(n1)
    is_int(n2)
    if n1 == n2:
        return n1

    common = common_denominator(n1, n2)

    return n1 * n2 // common
