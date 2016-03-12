# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

ZERO = 0
MIN = 100
MAX = 999

def isPalindrome(number):
    reverse = str(number)[::-1]
    if (str(number) == str(reverse)):
        return True
    else:
        return False

lhs = MAX
palindromes = []

while (lhs >= MIN):
    rhs = MAX;
    while (rhs >= MIN):
        palindrome = isPalindrome(lhs * rhs)
        if (palindrome):
            palindromes.append(lhs * rhs)
        rhs = rhs -1
    lhs = lhs - 1

print("The largest palindrome is: ", max(palindromes))
