import sys
from collections import deque

sys.stdin = open('input2.txt')

T = int(input())

def maze(data, start):
    # visited
    v = [[0]*(len(data)) for _ in range(len(data))]
    # queue
    q = []
    q.append(start)
    v[start[0]][start[1]] = 1
    # 4 cardinal points
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    result = []
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ti = i + di[k]
            tj = j + dj[k]
            t = data[ti][tj]
            if (t == 0 or t == 3) and not v[ti][tj]:
                q.append((ti, tj))
                v[ti][tj] = v[i][j] + 1
                if t == 3:
                    result.append(v[i][j])
    if result:
        return min(result)-1
    else:
        return 0

for tc in range(1, T+1):
    n = int(input())
    data = [[1]*(n+2)]
    for i in range(n):
        temp = list(map(int, input()))
        data.append([1]+temp+[1])
        if 2 in temp:
            start = (i+1, temp.index(2)+1)
    data.append([1]*(n+2))
    result = maze(data, start)
    print(f'#{tc} {result}')