#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    cntMax = 0
    cntMin = 0
    tempMax = scores[0]
    tempMin = scores[0]
    for i in scores:
        if tempMin > i:
            tempMin = i
            cntMin += 1
        elif tempMax < i:
            tempMax = i
            cntMax += 1
        else:
            pass

    return cntMax, cntMin


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
