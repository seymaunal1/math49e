import time

"""
This is a alternative solution for problem 8:
* Hadi_Hsn
* https://projecteuler.net/thread=8;page=5#446032
"""
"""
- Total time of alternative solution: 0.0003581047058105469
- Total time of my solution: 0.00042819976806640625

Main reason for this difference: They used a simple for loop to calculate the product of the digits instead of
using functions like map and reduce like I did. So these additional functions made my solution less efficient.

Or alternative answer:

Main reason for this difference is the function call overhead in my solution. While functions like map() and reduce() are elegant,
they require multiple lambda calls and the creation of intermediate list objects (e.g., list(result)).
The alternative solution uses a direct for loop to calculate the product. By avoiding lambda functions and extra object allocations,
the code executes more efficiently, leading to a faster overall runtime.
"""

begin = time.time()

def LargestAdjacentProduct():
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    num_str = str(num)
    potential_nums = []
    #get the possible 13 adjacent numbers without zero in it
    for i in range(len(num_str)):
        if i+14 <= len(num_str):
            potential_num = num_str[i:i+13]
            if "0" not in potential_num:
                potential_nums.append(potential_num)

    potential_nums = [GetProductofDigits(string) for string in potential_nums]

    return max(potential_nums)

def GetProductofDigits(string):
    product = 1
    for digit in string:
        product *= int(digit)
    return product

print(LargestAdjacentProduct())

end = time.time()
print(f"Finished in {end - begin} seconds.")

