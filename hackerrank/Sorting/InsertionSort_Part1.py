#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    remove = arr[-1]
    target = n - 2
    while remove < arr[target] and target >= 0:
        arr[target + 1] = arr[target]
        target -= 1
        print(' '.join(map(str, arr)))
    arr[target + 1] = remove
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
