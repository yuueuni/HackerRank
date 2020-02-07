import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    if n>m:
        mx = list(map(int, input().split()))
        mi = list(map(int, input().split()))
    else:
        mi = list(map(int, input().split()))
        mx = list(map(int, input().split()))
    res = []
    for c in range(abs(n-m)+1):
        temp_arr = list(mx[x] for x in range(c, c+len(mi)))
        sum_arr = sum(i*j for i, j in zip(mi, temp_arr))
        res.append(sum_arr)
    print(f'#{tc}', max(res))