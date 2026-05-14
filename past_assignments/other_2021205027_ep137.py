import time

"""
This is a alternative solution for problem 137:
* GerhardS
* https://projecteuler.net/quote_post=417886
"""
"""
- Total time of alternative solution: 1.6927719116210938e-05 seconds.
- Total time of my solution:   2.4080276489257812e-05 seconds.

Main reasons for this time difference:
Even though the time difference is so small, we can still see the efficiency differences between the codes.
In my code I wrote 3 seperate functions one to calculate fibonacci, one to calculate lucas numbers and
finally one to calculate golden nugget. Using three functions can make my code slightly slower.
Also, they calculate the fibonacci_k * fibonacci_k+1 when k = 15 which gives the 15th golden nugget directly,
Meanwhile I first calculated the fibonacci up to 4*15+1, then use them to find the Lucas number,
finally I calculated the golden nugget.


"""

begin = time.time()
# calculate the fibonacci number up to 30th index
fib, next_fib = 1, 1
for _ in range(2, 2 * 15 + 1):
    fib, next_fib = next_fib, fib + next_fib
# fibonacci_k * fibonacci_k+1 for k = 15 gives the 15th golden nugget.
print(f"result of the problem 137 {fib * next_fib}")

end = time.time()
print(f"Finished in {end - begin} seconds.")
