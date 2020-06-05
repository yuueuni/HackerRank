import sys

sys.stdin = open('input.txt')

T = int(input())   

def find(n, b, k, cur):
    global ans
    if b <= cur < ans:
        ans = cur
    if k == n:
        return
    else:
        a[k] = 1
        find(n, b, k+1, cur+data[k])
        a[k] = 0
        find(n, b, k+1, cur)

for tc in range(1, T+1):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))
    a = [0]*n
    ans = 100000
    find(n, b, 0, 0)
    print(f'#{tc} {ans-b}')