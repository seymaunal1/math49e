import operator
import time
from functools import reduce


def solve_problem_8() -> None:
    # Input numbers as string
    numbers: str = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )

    #  Number of adjacent digits to evaluate per slice
    lookahead: int = 13

    results: list[str] = []
    # Iterate through the string using for loop
    for index in range(0, len(numbers) - (lookahead - 1)):
        current_result: str = numbers[index : index + lookahead]

        #  Optimization step:
        #  Zero can not be inside in this 13 adjacent group, otherwise the result will be zero.
        if "0" not in current_result:
            results.append(current_result)

    # Compute the product of digits for each valid slice, then return the maximum product found.
    # To be able to do that:
    # - Convert each character to integer
    # - Multiply digits using reduce and multiplication operator
    # - Compare all results and find the maximum
    print(
        max(
            map(
                lambda result: reduce(
                    operator.mul, map(lambda value: int(value), list(result)), 1
                ),
                results,
            )
        )
    )


# To keep the program structure clear and readable
if __name__ == "__main__":
    begin = time.perf_counter()
    solve_problem_8()
    end = time.perf_counter()
    print(f"Finished in {end - begin} seconds.")
