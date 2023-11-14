#!/bin/python3
import math
import os
import random
import re
import sys
import itertools


# Complete the superReducedString function below.
def superReducedString(s):
    answer = ''
    for i in range(len(s)):
        temp = s[i]
        if len(answer) == 0:
            answer += temp
        elif answer[-1] == temp:
            answer = answer[:-1]
        else:
            answer += temp
        
    if len(answer)==0:
        answer = "Empty String"
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
