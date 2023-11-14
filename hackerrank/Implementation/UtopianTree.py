#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    answer = 1
    period = 0
    while n > period:
        if period % 2 == 0:
            answer *= 2
            period += 1
        elif period % 2 == 1:
            answer += 1
            period += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
