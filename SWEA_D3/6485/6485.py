import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    station = {i:0 for i in range(1, 5001)}
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            station[i] += 1
    p = int(input())
    print(f'#{tc}', end=' ')
    for _ in range(p):
        c = int(input())
        print(station[c], end=' ')
    print()
