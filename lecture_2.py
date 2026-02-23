# 23.02.2026


import time

# problem 104
# TO DO

# Problem 57:
def continued_fraction():
    elements = [1]
    for _ in range(999):
        elements.append(2)

    numerators = [1, 3]
    denominators = [1, 2]

    for i in range(2, len(elements)):
        numerators.append(elements[i] * numerators[i - 1] + numerators[i - 2])
        denominators.append(elements[i] * denominators[i - 1] + denominators[i-2])

    digit_counts_numerators = [len(str(abs(n))) for n in numerators]
    digit_counts_denominators = [len(str(abs(n))) for n in denominators]
    sum = 0
    for i in range(len(digit_counts_denominators)):
        if digit_counts_numerators[i] > digit_counts_denominators[i]:
            sum += 1
    print(sum)



# Problem 64:
# last term of the period is equal to twice time of the initial term a_0



if __name__ == "__main__":
    begin = time.time()
    continued_fraction()
    end = time.time()
    print(f"Finished in {end - begin} seconds.")
