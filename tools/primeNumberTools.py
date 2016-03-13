import math

def determineIfPrime(possiblePrime):
    isPrime = True
    for num in range(2, math.ceil(possiblePrime) -1):
        if (possiblePrime % num == 0):
            isPrime = False
            break
    return isPrime
