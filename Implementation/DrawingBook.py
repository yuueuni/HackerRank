#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    cnt = min(p//2, n//2-p//2)
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
