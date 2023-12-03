#!/bin/python3

import math
import os
import random
import re
import sys
from array import array
from bisect import bisect_left, insort


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    cnt = 0
    mid = d // 2
    is_odd = d % 2

    sorted_exp = sorted(expenditure[:d])

    for key, value in enumerate(expenditure[d:], d-1):
        x = expenditure[key - d]
        if key != d - 1 and x != expenditure[key]:
            idx = bisect_left(sorted_exp, x)
            sorted_exp.pop(idx)
            insort(sorted_exp, expenditure[key])

        median = sorted_exp[mid] * 2 if is_odd else sorted_exp[mid] + sorted_exp[mid - 1]
        if value >= median:
            cnt += 1
    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    n = 9

    # d = int(first_multiple_input[1])
    d = 5

    # expenditure = list(map(int, input().rstrip().split()))
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

    result = activityNotifications(expenditure, d)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
