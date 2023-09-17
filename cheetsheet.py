from collections import defaultdict
from itertools import product, combinations, permutations

import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**7)
# num = sys.stdin.readline().strip()

sign = [-1, 1]
prods = list(product(sign, repeat=3))
print(prods)


