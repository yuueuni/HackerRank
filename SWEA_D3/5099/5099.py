import sys

sys.stdin = open('input.txt')

T = int(input())


def melt(data, n):
    m = [data.pop(0) for _ in range(n)]
    idx = [i for i in range(1, n+1)]
    c = n+1
    while m:
        temp = m.pop(0)//2
        tidx = idx.pop(0)
        if temp:
            m.append(temp)
            idx.append(tidx)
        else:
            if data:
                m.append(data.pop(0))
                idx.append(c)
                c += 1
    return tidx
        


for tc in range(1, T+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    data = cheese
    result = melt(data, n)
    print(f'#{tc} {result}')