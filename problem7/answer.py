# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

from tools.primeNumberTools import determineIfPrime

def init():
    MAX = 10001
    current = 1
    count = 0;
    currentPrime = 0
    while (count < MAX):
        current = current + 1
        isprime = determineIfPrime(current)
        if(isprime):
            count = count + 1
            currentPrime = current
    print(currentPrime)
