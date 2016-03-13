# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from tools.primeNumberTools import determineIfPrime

def init():
    MAX = 2000000
    primes = []
    for number in range(2, MAX):
        isprime = determineIfPrime(number)
        if(isprime):
            primes.append(number)
    primesum = 0
    for number in primes:
        primesum = primesum + number
    print(primesum)
