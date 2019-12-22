import itertools


def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num


def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
