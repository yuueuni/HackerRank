#!/bin/python3
import copy
import math
import os
import random
import re
import sys


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    asc_count = desc_count = 0
    desc_arr = copy.deepcopy(arr)
    sort_arr = sorted(arr)
    sort_arr_desc = sorted(arr, reverse=True)
    asc_dict = {}
    desc_dict = {}
    for i in range(len(arr)):
        asc_dict[arr[i]] = i
        desc_dict[arr[i]] = i

    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            idx = asc_dict[sort_arr[i]]
            arr[i], arr[idx] = arr[idx], arr[i]
            asc_dict[arr[i]] = i
            asc_dict[arr[idx]] = idx
            asc_count += 1

        if desc_arr[i] != sort_arr_desc[i]:
            idx = desc_dict[sort_arr_desc[i]]
            desc_arr[i], desc_arr[idx] = desc_arr[idx], desc_arr[i]
            desc_dict[desc_arr[i]] = i
            desc_dict[desc_arr[idx]] = idx
            desc_count += 1

    return asc_count if asc_count < desc_count else desc_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = [3, 4, 2, 5, 1]

    result = lilysHomework(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
