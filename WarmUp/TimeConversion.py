#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#

def timeConversion(s):
    temp = s[-2:]
    hh = s[:2]
    mmss = s[2:-2]

    if temp == "AM":
        if hh == "12":
            answer = "00" + mmss
        else:
            answer = hh + mmss
    else:
        if hh == "12":
            answer = hh + mmss
        else:
            answer = str(int(hh) + 12) + mmss

    return answer


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
