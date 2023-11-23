#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    left, right = [], []
    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
    return left + [pivot] + right

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))
    arr = [4, 5, 3, 7, 2]
    result = quickSort(arr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
