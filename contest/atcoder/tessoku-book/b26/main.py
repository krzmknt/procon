from collections import deque
import bisect
import copy
import heapq
import itertools
import math
import string

import sys

sys.setrecursionlimit(10**7)


(n, m), *a = [[*map(int, l.split())] for l in open(0)]
