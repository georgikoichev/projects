from projects.primes_operations import is_prime
from projects.validation import is_int

def is_perfect(n):
    is_int(n)
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return sum(factors) == n

def all_perfect(n):
    is_int(n)
    perfect = []
    for i in range(2, n + 1):
        a = 2 ** i - 1
        b = a * (2 ** (i-1))
        if b > n:
            break
        if is_prime(a):
            perfect.append(b)

    return perfect or None