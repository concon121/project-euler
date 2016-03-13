# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def init():
    TO_FIND = 1000
    start = 1
    combo = []
    for a in range (start, TO_FIND):
        for b in range(a+1, TO_FIND):
            for c in range(b+1, TO_FIND):
                if (a + b + c == TO_FIND):
                    a2 = a * a
                    b2 = b * b
                    c2 = c * c
                    product = a * b * c
                    if (a2 + b2 == c2):
                        combo.append(a)
                        combo.append(b)
                        combo.append(c)
                        combo.append(product)
                        break
        start = start +1
    print(combo)
