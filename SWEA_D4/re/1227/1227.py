import sys

sys.stdin = open('input.txt')

def dfs(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    s = []
    visited = [ [0]*100 for _ in range(100)]
    s.append((i, j))
    visited[i][j] = 1
    while s:
        i, j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni > 99 or nj > 99 or ni < 0 or nj < 0:
                break
            if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                s.append((ni, nj))
                visited[ni][nj] = 1
    return 0


for tc in range(1, 11):
    T = int(input())
    maze = [ list(input()) for _ in range(100) ]
    si, sj = -1, -1
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    
    r = dfs(si, sj)
    print(f'#{T} {r}')