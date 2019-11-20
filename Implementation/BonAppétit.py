#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    halfBill = sum(bill)/2
    annaBill = (sum(bill)-bill[k])/2
    if annaBill == b:
        print("Bon Appetit")
    else:
        temp = halfBill - annaBill
        print("%g"%temp)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
