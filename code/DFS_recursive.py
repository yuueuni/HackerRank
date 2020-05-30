# import sys

# sys.stdin = open('input.txt')

T = int(input())

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def checkrange(n, m):
    if 0<=n<10 and 0<=m<10:
        return 1
    else:
        return 0

def find(i, j, data):
    visited[i][j] = 1
    for k in range(8):
        ti = i + di[k]
        tj = j + dj[k]
        if checkrange(ti, tj) and data[ti][tj] and not visited[ti][tj]:
            find(ti, tj, data)


for tc in range(1, T+1):
    visited = [[0]*10 for _ in range(10)]
    data = [list(map(int, input().split())) for _ in range(10)]
    cnt = 0
    for x in range(10):
        for y in range(10):
            if data[x][y] and not visited[x][y]:
                find(x, y, data)
                cnt += 1
    print(f'#{tc} {cnt}')