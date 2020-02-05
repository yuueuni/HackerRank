import sys


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    test = input()
    s = []
    balance = True
    idx = 0

    while idx < len(test) and balance:
        temp = test[idx]

        if temp == '(' or temp == '{':
            s.append(temp)
        else:
            if s:
                balance = False
            else:
                s.pop()

        idx += 1

    if balance and s:
        result = True
    else:
        result = False
    print(result)