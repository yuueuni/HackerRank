import sys

sys.stdin = open('input.txt')

T = int(input())

primeNumber = []
for i in range(2, 1000):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        primeNumber.append(i)

# def check(number):
#     return 1


for tc in range(1, T+1):
    n = int(input())
    result = check(n)
    cnt = 0
    print(f'#{tc} {cnt}')
