import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    node = [0 for _ in range(n+2)]
    for _ in range(m):
        idx, num = map(int, input().split())
        node[idx] = num
    if n%2:
        for i in range(n, 1, -2):
            node[i//2] = node[i] + node[i-1]
    else:
        for i in range(n+1, 1, -2):
            node[i//2] = node[i] + node[i-1]
    print(f'#{tc} {node[l]}')