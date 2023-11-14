#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr, n):
    plus, minus, zero = 0, 0, 0
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1
    
    answer = str(round(plus/n, 6)) + "\n" + str(round(minus/n, 6)) + "\n" + str(round(zero/n, 6))
    print(answer)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
