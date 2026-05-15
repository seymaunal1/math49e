# type: ignore

# repunit: repeated unit, all digits is equal to one
# problem 132:

# this can be written as a geometric functions 10^k -1 / 9

# the prime numbers that divide this series is p ; 9p|10^k -1 so p | 10^k -1
# 10^k = 1 (mod p)
# find order of an element in a finite group; smallest order that makes the number identity
# eratosthenes sieve problem

from math import gcd


def order_of_a_modulo(a, n):
    i = 1
    while i > 0:
        if a**i % n == 1:
            return i
        else:
            i += 1


def ord_of_mod(a, n):
    if gcd(a, n) != 1:
        return 0
    if gcd(a, n) == 1:
        i = 1
        while pow(a, i, n) != 1:
            i += 1
        return i


def prime_sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)

    return primes


counter_ = 0
sum_ = 0
for p in prime_sieve(100000):
    if p > 3:
        order = order_of_a_modulo(10, p)
        if order != -1 and pow(10, gcd(10**9, p - 1, p)) % p == 1:
            sum_ = sum_ + p
            counter_ = counter_ + 1
        if counter_ == 40:
            break
print(counter_)
print(sum_)
