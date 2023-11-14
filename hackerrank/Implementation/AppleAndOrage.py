#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ansA = [x+a for x in apples]
    ansO = [x+b for x in oranges]
    cntA, cntO = 0, 0

    for i in ansA:
        if s <= i <= t :
            cntA += 1
        
    for j in ansO:
        if s <= j <= t :
            cntO += 1
    
    print(cntA)
    print(cntO)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
