# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

focus = 600851475143
divisor = 3
found = 0;

def determineIfPrime(possiblePrime):
    isPrime = 1
    for num in range(2, math.ceil(possiblePrime) -1):
        if (possiblePrime % num == 0):
            isPrime = 0
            break
    return isPrime


while (found == 0):
    if (focus % divisor == 0):
        found = determineIfPrime(focus / divisor)
        if (found == 1):
            print(focus / divisor)
    divisor = divisor + 1
