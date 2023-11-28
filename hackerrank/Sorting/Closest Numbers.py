#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    result = {}
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff in result:
            result[diff].extend([arr[i], arr[i+1]])
        else:
            result[diff] = [arr[i], arr[i + 1]]
    diff_keys = list(result.keys())
    min_diff = sorted(diff_keys)[0]
    return result[min_diff]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/Closest Numbers input.txt')
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    print(' '.join(map(str, result)))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
    sys.stdin = open('/Users/yoonp/repo/algorithm/hackerrank/Sorting/Closest Numbers result.txt')
    res_e = input().rstrip().split()
    print(res_e)
