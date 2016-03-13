# The sum of the squares of the first ten natural numbers is,

# 1^1 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

MIN = 1
MAX = 100

squareSum = 0

for number in range(MIN, MAX+1):
    square = number * number
    squareSum = squareSum + square

sumToSquare = 0

for number in range(MIN, MAX+1):
    sumToSquare = sumToSquare + number

sumSquared = sumToSquare * sumToSquare

difference = sumSquared - squareSum

print(sumSquared, " - ", squareSum, " = ", difference)
