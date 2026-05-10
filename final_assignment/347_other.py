import math
import time

"""
This is a alternative solution for problem 469:
* SAG145
* https://projecteuler.net/quote_post=428974


- Total time of alternative solution: 1.580787583021447 seconds.
- Total time of my solution: 1.858215093612671 seconds.
- The result: 11109800204052

The main reason for this difference:

The alternative solution is slightly faster because it limits the search space earlier.
It only uses possible p values up to sqrt(N), and uses logarithms to estimate the
maximum powers of p and q.

My solution is more direct: it checks prime pairs and generates powers with while loops.
Both solutions use the same idea, but the alternative code avoids some unnecessary checks.

Also another reason is that: they checked all the primes up to N//2, meanwhile I checked until N

"""


begin = time.time()
# they find all the primes up to N//2
def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    # Collect prime numbers into a list
    primes_list = []
    for k in range(n):
        if primes_bool[k]:
            primes_list.append(k)
    return primes_list

def log(a,b):
    # returns the limit of numbers of powers
    return math.floor(math.log(b,a)) + 1

def M(p,q,N):
    # Find the largest p^lp * q^lq <= N
    max = 0
    # Try powers of p that holds the condition
    for lp in range(1,log(p,N / q)):
        # Try powers of p that holds the condition
        for lq in range(1,log(q,N / p)):
            res = p**lp*q**lq
            if res < N + 1:
                if res > max:
                    max = res
    return max

def S(N):
    # All possible prime values up to N//2
    primes = all_primes_below_n(N // 2)
    # p only needs to go up to sqrt(N)
    good_p = all_primes_below_n(math.floor(math.sqrt(N)))
    sum = 0
    # Choose p from smaller prime list
    for p in range(len(good_p)):
        # Choose q after p to keep p < q
        for q in range(p + 1,len(primes)):
            # Calculate M for prime pair
            m = M(primes[p],primes[q],N)
            sum += m
            # If M is 0, q is too large, so stop this inner loop
            if m == 0:
                break
    return sum

print(S(10**7))
end = time.time()
print(f"Finished in {end - begin} seconds.")
