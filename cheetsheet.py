from collections import defaultdict
from itertools import product, combinations, permutations
from functools import cmp_to_key

import sys
input = sys.stdin.readline
write = sys.stdout.write

sys.setrecursionlimit(10**5)
# too large number of setrecursionlimit in Pypy3 can cause use of large stack memory. 

# num = sys.stdin.readline().strip()

sign = [-1, 1]
prods = list(product(sign, repeat=3))
print(prods)


