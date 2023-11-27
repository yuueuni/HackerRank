#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    sorting = [[] for _ in range(len(arr))]
    for idx in range(len(arr)):
        value = arr[idx]
        number, string = value
        if idx < len(arr) // 2:
            sorting[int(number)] += '-'
        else:
            sorting[int(number)] += [string]
    result = []
    for s in sorting:
        result.extend(s)
    print(' '.join(result))

if __name__ == '__main__':
    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/The Full Counting Sort input.txt')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    res = countSort(arr)

    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/The Full Counting Sort result.txt')
    res_e = input().rstrip().split()
    print(res_e)
