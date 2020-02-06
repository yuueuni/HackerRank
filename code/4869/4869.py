import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = n // 20
    if d%2:
        result = (2**(d-1))*4+1
    else:
        result = (2**(d-1))*4

    print(f'#{tc} {result}')