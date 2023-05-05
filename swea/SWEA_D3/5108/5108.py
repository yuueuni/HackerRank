import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(m):
        idx, number = map(int, input().split())
        data.insert(idx, number)
    print(f'#{tc}', data[l])