from array import array

N = 10_000_000
# to determine the last 18 digits
MOD = 10**18


# we labeled all the prime up to n with that sieve function
def sieve(n):
    comp = bytearray(n + 1)
    comp[0] = comp[1] = 1

    for i in range(2, int(n**0.5) + 1):
        if not comp[i]:
            comp[i * i : n + 1 : i] = b"\x01" * (((n - i * i) // i) + 1)
    return comp


print(sieve(n=100))


# Tonelli - Shanks Algorithm:
# z ** ((p - 1)/2
def sqrt_minus_one(p):
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    return pow(z, (p - 1) // 4, p)


def solve(n):
    limit = 2 * n
    comp = sieve(limit)

    rem = array("Q", (4 * k**2 + 1 for k in range(n + 1)))
    best = array("Q", [0]) * (n + 1)

    for p in range(5, limit + 1, 4):
        if comp[p]:
            continue

        root = sqrt_minus_one(p)
        inv2 = (p + 1) // 2

        r1 = root * inv2 % p
        r2 = (-r1) % p

        for r in (r1, r2):
            if r == 0:
                r = p

            for k in range(r, n + 1, p):
                while rem[k] % p == 0:
                    rem[k] //= p
                best[k] = p

    ans = 0

    for k in range(1, n + 1):
        ans = (ans + max(best[k], rem[k])) % MOD

    return ans


print(f"{solve(N):018d}")
