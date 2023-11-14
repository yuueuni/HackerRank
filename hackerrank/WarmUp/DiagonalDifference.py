#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumArr = 0
    sumRevArr = 0
    l = len(arr)
    for i in range(l):
        temp1 = arr[i][i]
        temp2 = arr[i][l-i-1]
        sumArr += temp1
        sumRevArr += temp2
    
    answer = abs(sumArr - sumRevArr)
    return answer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
