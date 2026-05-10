import time

begin = time.time()

"""
This is a alternative solution for problem 340:
* _syne
* https://projecteuler.net/quote_post=36245

- Total time of alternative solution: 2.6226043701171875e-06 seconds.
- Total time of my solution: 3.814697265625e-06 seconds.
- Result of problem 340 is 291504964.

The main difference of the code:
- My solution first derives the summation formula directly from the expanded form of F(n):
* F(n) = (k + 1) * a - c + n + (k + 1) * 3 * (a - c)
Then I split the total sum into three separate parts.
So, my code computes the total by explicitly calculating each part of the summation.

- Their solution uses a more compressed form of F(n):
* F(n) = ((b - n) // a) * (4*a - 3*c) + 4*(a-c) + n
The other solution notices that F(n) behaves like an arithmetic sequence on each block.
So, the code can compute the total using arithmetic sequence sums, since (b-n)//a is fixed on some intervals,
instead of explicitly separating summation into 3 parts.
* Even though my code is more clear and follows the mathematical algorithm more, their solution is
shorter and more optimized because it uses the linear structure of F(n).
"""

a, b, c = 21**7, 7**21, 12**7
# to understand how many a in b-n: (b-n)//a
# F(n) is written in its simplified closed form.
def F(n):
  return ((b-n)//a) * (4*a-3*c) + 4*(a-c) + n

def S():
  # t is the remainder when b is divided by a.
  # It separates the last incomplete block from the full blocks.
  t = b%a
  # F(n) forms arithmetic sequences on these blocks.
  # number_of_terms * (first_term + last_term) / 2
  return ( (b-t) * (F(b)+F(t+1)) + (t+1) * (F(t)+F(0)) ) // 2

print(S())


end= time.time()
print(f"Finished in {end - begin} seconds.")
