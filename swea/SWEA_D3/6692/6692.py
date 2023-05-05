import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    res = 0
    for _ in range(n):
        p, x = map(float, input().split())
        res += p*x
    print(f'#{tc}', '%.6f' % res)
