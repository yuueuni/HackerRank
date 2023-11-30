#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    idx = 1
    shift = 0
    while idx != len(arr):
        if arr[idx - 1] > arr[idx]:
            for i in range(idx):
                if arr[i] > arr[idx]:
                    arr.insert(i, arr.pop(idx))
                    shift += idx - i
                    break
        idx += 1
    return shift


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())
    t = 1
    for t_itr in range(t):
        # n = int(input().strip())
        n = 5

        # arr = list(map(int, input().rstrip().split()))
        arr = [2, 1, 3, 1, 2]

        result = insertionSort(arr)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
