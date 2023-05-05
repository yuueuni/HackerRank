import sys

sys.stdin = open('input.txt')


T = int(input())

def find(i, j, ni):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    s = []
    s.append((i, j))
    visited[i][j] = 1
    while s:
        i, j = s.pop()
        if data[i][j] == '3':
            return 1
        for k in range(4):
            ti = i + di[k]
            tj = j + dj[k]
            if ti > (ni-1) or tj > (ni-1) or ti < 0 or tj < 0:
                continue
            if data[ti][tj] != '1' and visited[ti][tj] == 0:
                s.append((ti, tj))
                visited[ti][tj] = 1
    return 0


for tc in range(1, T+1):
    n = int(input())
    data = []
    visited = [ [0]*n for _ in range(n)]
    for idx in range(n):
        temp = list(input())
        data.append(temp)
        if '2' in temp:
            si, sj = idx, temp.index('2')
    
    result = find(si, sj, n)
    print(f'#{tc} {result}')