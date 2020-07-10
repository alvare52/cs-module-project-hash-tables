"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
import random

# Plan
# pick 4 random numbers in q (can be duplicates)
# assign a, b, c, d

# put (a, b, c, d) in here?
cache = {} 

# pick 4 random nums in q
a = random.choice(q)
b = random.choice(q)
c = random.choice(q)
d = random.choice(q)

print("\n--- START ---\n")
# print("f(x) = x * 4 + 6")

print(f"f({a}) | f({b}) | f({c}) | f({d})")
print(f" {f(a)}  +  {f(b)}  =  {f(c)}  -  {f(d)}")

print("\n--- END ---\n")