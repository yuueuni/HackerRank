#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for idx in range(2, n+1):
        temp = sorted(arr[:idx], key=lambda x: x)
        arr = temp + arr[idx:]
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # insertionSort2(n, arr)
    insertionSort2(6, [1, 4, 3, 5, 6, 2])
