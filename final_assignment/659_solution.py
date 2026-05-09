from array import array
from math import isqrt

N = 10_000_000
LIMIT = 2 * N
MOD = 10**18


def sieve(limit):
    is_comp = bytearray(limit + 1)
    primes = []

    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes.append(i)
            if i * i <= limit:
                step = i
                start = i * i
                is_comp[start:limit + 1:step] = b"\x01" * (((limit - start) // step) + 1)

    return primes


def mod_pow(a, e, m):
    result = 1
    while e:
        if e & 1:
            result = result * a % m
        a = a * a % m
        e >>= 1
    return result


def tonelli_shanks(n, p):
    """
    x^2 = n mod p çözümü.
    Bu problemde n = p - 1, yani -1 mod p.
    p asal olmalı.
    """
    if p == 2:
        return n

    if mod_pow(n, (p - 1) // 2, p) != 1:
        return None

    if p % 4 == 3:
        return mod_pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while mod_pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = mod_pow(z, q, p)
    x = mod_pow(n, (q + 1) // 2, p)
    t = mod_pow(n, q, p)
    m = s

    while t != 1:
        i = 1
        temp = t * t % p

        while temp != 1:
            temp = temp * temp % p
            i += 1

        b = mod_pow(c, 1 << (m - i - 1), p)
        x = x * b % p
        c = b * b % p
        t = t * c % p
        m = i

    return x


def solve(n=N):
    limit = 2 * n
    primes = sieve(limit)

    # rem[k] = 4k^2 + 1'in küçük asal çarpanları bölündükten sonra kalan kısmı
    rem = array("Q", [0]) * (n + 1)

    # largest[k] = şimdiye kadar bulunan en büyük asal çarpan
    largest = array("I", [0]) * (n + 1)

    for k in range(1, n + 1):
        rem[k] = 4 * k * k + 1

    for p in primes:
        if p < 5:
            continue
        if p % 4 != 1:
            continue

        x = tonelli_shanks(p - 1, p)

        inv2 = (p + 1) // 2
        r1 = x * inv2 % p
        r2 = (-r1) % p

        if r1 == 0:
            r1 = p
        if r2 == 0:
            r2 = p

        for r in (r1, r2):
            if r > n:
                continue

            for k in range(r, n + 1, p):
                while rem[k] % p == 0:
                    rem[k] //= p
                largest[k] = p

    ans = 0

    for k in range(1, n + 1):
        lpf = largest[k]

        if rem[k] > 1 and rem[k] > lpf:
            lpf = rem[k]

        ans = (ans + lpf) % MOD

    return ans


if __name__ == "__main__":
    print(f"{solve():018d}")
