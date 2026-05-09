import time
from math import factorial

"""
This is a alternative solution for problem 469:
* ofir
* https://projecteuler.net/quote_post=166206
"""
"""
- Total time of alternative solution: 9.202957153320312e-05 seconds.
- Total time of my solution: 0.08853292465209961
- The result: 0.56766764161831

The main reason for this difference:
* Their solution directly uses the closed-form summation for f(n),
  f(m) = sum((-2)^(k-1) * (m-k+1) / k!)
while my code first defines the linear expected value A_n recursively and then uses its limit.

* In their code, the infinite series is approximated by summing the first 100 terms,
In my code, I use the fact that for very large n to calculate limit of A(n).
So, the alternative solution is faster because it does not build the recursive
A_n sequence and does not use decimal arithmetic. It only evaluates a short
100-term summation using the closed-form formula.
"""
begin = time.time()
n = 10**18
# they directly calculate series:  f(m) = sum((-2)^(k-1) * (m-k+1) / k!) ~ ((1 - e **2) / 2) up to 100
print('%.14f' % (1-(sum((-2)**(k-1)*(n-3-k+1)/factorial(k) for k in range(1, 100))+1)/n))

end = time.time()
print(f"Finished in {end - begin} seconds.")

