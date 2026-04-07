import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def solve_problem_543() -> int:
    total = 2

    for i in range(4, 101):
        # üçten büyük tüm çift sayılar k=1 i tutmaz k=2 yi tutar goldbach conjecture
        if i > 3 and i % 2 == 0:
            par_number = i // 2 - 1
        # üçte büyük tek sayılar
        else:
            # prime olanlar her zaman k = 1 tutar
            if is_prime(i):
                # 2 çıkarıldığında prime olan hali de her zaman k 2 yi tutar
                if is_prime(i - 2):
                    par_number = i // 2
                # 2 çıkarıldığında prime olmayan hali de her zaman k 2 yi tutmaz
                else:
                    par_number = i // 2 - 1
            # tek ama prime olmayanlar. k 1 tutmaz, bu durudma k 2 yi çek ederiz
            else:
                if is_prime(i - 2):
                    par_number = i // 2 - 1

                else:
                    par_number = i // 2 - 2
        total += par_number

    return total


# 44th element of fibonacci 1134903170, n should be equal to 1134903170

"""
çift  par_number = i // 2 - 1
total number(i//2 ** i//2 - 1 ) / 2

fibonacci sequence of 44 elements:
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
832040, 1346269, 2178309, 3524578, 5702887, 9227465,14930352, 24157817, 39088169,
63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]

"""

if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_543()
    end = time.perf_counter()

    print(f"Result of problem 543 is {result}.")
    print(f"Finished in {end - begin} seconds.")
