import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    D = sys.stdin.readline().strip()
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')


#-------------version 2-----------------
for _ in range(T):
    stack = 0
    D = sys.stdin.readline().strip()
    for p in D:
        if p == '(':
            stack += 1
        else:
            if stack != 0:
                stack -= 1
            else:
                print('NO')
                break
    else:
        if stack == 0:
            print('YES')
        else:
            print('NO')