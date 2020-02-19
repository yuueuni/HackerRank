import sys

sys.stdin = open('input.txt')

# for _ in range(10):
#     T = int(input())
#     data = []
#     for i in range(16):
#         data.append(list(map(int, input())))
#     print(f'#{T}')
#     print(*data, sep='\n')
# --------------------------------


# def dfs(i, j, mazei):
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]

#     if mazei[i][j] == '3':
#         return 1
#     else:
#         mazei[i][j] = '1'
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if mazei[ni][nj] != '1':
#                 if dfs(ni, nj, mazei) == 1:
#                     return 1
#         return 0

def dfs(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    s = []
    visited = [ [0]*16 for _ in range(16)]
    s.append((i, j))
    visited[i][j] = 1
    while len(s)!=0:
        i, j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                s.append((ni, nj))
                visited[ni][nj] = 1
    return 0




for tc in range(1, 11):
    T = int(input())
    maze = [ list(input()) for _ in range(16) ]
    si, sj = -1, -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    
    r = dfs(si, sj)
    print(f'#{T} {r}')