# Given an integer n, the task is to compute its factorial, i.e.
# the product of all positive integers from 1 to n. Factorial is 
# represented as n! and is commonly used in mathematics, permutations 
# and combinatorics. 
# For Example:
# Input: n = 6
# Output: 720
# Explanation: 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720

#program
#Method 1:-

import math
n=6
print(math.factorial(n))

#method 2:-

n=6
if n<0:
    print ("no factorial defined for negative no.")
else:
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)
    