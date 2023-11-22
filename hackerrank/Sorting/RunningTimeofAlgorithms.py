#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    shift = 0
    for i in range(0, len(arr)):
        target = i
        while 0 <= target < len(arr) - 1:
            if arr[target] > arr[target + 1]:
                arr[target + 1], arr[target] = arr[target], arr[target + 1]
                shift += 1
                target -= 1
            else:
                break
    return shift
#
# 0           2 1 3 1 2
# 1           1 2 3 1 2     1
# 2           1 2 3 1 2     0
# 3           1 1 2 3 2     2
# 4           1 1 2 2 3     1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))
    # arr = [4, 4, 3, 4]
    arr = [2, 1, 3, 1, 2]

    result = runningTime(arr)
    print('+++++++' + str(result))

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
