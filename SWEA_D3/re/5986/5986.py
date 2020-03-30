import sys

sys.stdin = open('input.txt')

T = int(input())

def primeNumber(number):
    printN = []
    for i in range(2, number+1):
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            printN.append(i)
    return printN

def check(number):
    pn = primeNumber(number)
    temp = []
    


for tc in range(1, T+1):
    n = int(input())
    result = primeNumber(n)
    print(f'{tc} {result}')
