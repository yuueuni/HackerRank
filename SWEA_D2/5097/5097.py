import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = m % n
    while cnt:
        temp = data.pop(0)
        data.append(temp)
        cnt -= 1
    print(f'#{tc} {data[0]}')