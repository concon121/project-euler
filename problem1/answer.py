# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0

def returnIfMultipleOf3Or5(input):
    if (input % 3 == 0) or (input % 5 == 0):
        return input
    else:
        return 0

start = 1000

while start > 0:
    start = start - 1
    total = total + returnIfMultipleOf3Or5(start)

print (total)
