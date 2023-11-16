#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    return sorted(unsorted, key=lambda x: (len(x), x))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    unsorted = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']

    # for _ in range(n):
    #     unsorted_item = input()
    #     unsorted.append(str(unsorted_item))

    result = bigSorting(unsorted)
    print('answer')
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    #
    # fptr.close()
