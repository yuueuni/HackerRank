#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    s = list(zip(list(ascii_lowercase), h))
    t = {x:y for x,y in s}
    temp = [0] * len(word)
    for i in range(len(word)):
        temp[i] = t[word[i]]
    answer = max(temp) * len(word)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
