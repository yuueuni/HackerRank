#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = [0] * 100
    for a in arr:
        result[a] += 1
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/Counting Sort 1 input.txt')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)

    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/Counting Sort 1 result.txt')
    res = list(map(int, input().rstrip().split()))
    print(res)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
