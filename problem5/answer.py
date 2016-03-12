# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

MIN = 1
MAX = 20

start = 0
found = False
while (not found):
    start = start + 1
    thisFound = True
    for number in range(MIN, MAX):
        #print("Start: ", start)
        #print("Number", number)
        if (start % number != 0):
            thisFound = False
            break
    found = thisFound

print(start)
