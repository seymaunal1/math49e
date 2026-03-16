import time

"""
This is a alternative solution for problem 78:
* Katterin
* https://projecteuler.net/quote_post=434757

"""
"""
- Total time of alternative solution: 3.458164930343628 seconds seconds.
- Total time of my solution: 4.212154150009155 seconds.

Main reason for this difference:
* I called the function that calculates the pentagonal numbers every time.
However, they store all pentagonal numbers in one single list.
* I recalculate every pentagonal at every step, while they calculated them just once and reused them.
* My code uses recursion and they used iteration which usually makes it more efficient than using recursion.

"""

begin = time.time()
limit = 100000

pentagonals = []
odd = True
n = 1
p = n * (3 * n - 1) // 2
while p < limit:
    pentagonals.append(p)
    if odd:
        n = -n
    else:
        n = -n + 1
    odd = not odd
    p = n * (3 * n - 1) // 2

partitions = [1]
for i in range(1, limit + 1):
    count = 0
    total = 0
    terms = [j for j in pentagonals if j <= i]
    for term in terms:
        if count % 4 < 2:
            total += partitions[i - term]
        else:
            total -= partitions[i - term]
        count += 1
    partitions.append(total)
    if total % 1000000 == 0:
        print(i)
        break


end = time.time()

print(f"Finished in {end - begin} seconds.")
