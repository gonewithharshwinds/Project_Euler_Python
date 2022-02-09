# ================================================================
# Project Euler Problem 1
# ================================================================
# Copyright © gonewithharshwinds @ 2022. All rights reserved.
# ================================================================
# https://github.com/gonewithharshwinds/Project-Euler-Python
# ================================================================

def solve():
	s = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(s)

if __name__ == "__main__":
	print(solve())