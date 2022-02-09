# ================================================================
# Project Euler Problem 2 : Even Fibonacci numbers
# ================================================================
# Copyright © gonewithharshwinds @ 2022. All rights reserved.
# ================================================================
# https://github.com/gonewithharshwinds/Project-Euler-Python
# ================================================================
def solve():
    s,a,b = 0,1,2
    while a <= 4000000:
        if a % 2 == 0:
            s += a
        a, b = b, a + b
    return str(s)

if __name__ == "__main__":
    print(solve())