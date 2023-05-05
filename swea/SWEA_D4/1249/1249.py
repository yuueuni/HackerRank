import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\1249\\input.txt')

import heapq

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    data = [ list(map(int, input())) for _ in range(n) ]
    INF = float('inf')
    
    visited = [ [INF]*n for _ in range(n)]
    visited[0][0] = 0

    s = []
    heapq.heappush(s, (0, 0))

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    while s:
        i, j = heapq.heappop(s)
        for k in range(4):
            ti = i + di[k]
            tj = j + dj[k]
            if 0 <= ti < n and 0 <= tj < n:
                temp = visited[i][j] + data[ti][tj]
                if visited[ti][tj] > temp:
                    visited[ti][tj] = temp
                    heapq.heappush(s, (ti, tj))

    print(f'#{tc}', visited[-1][-1])

# ------------------------------------------------------------
# def find(n):
#     s = []
#     heapq.heappush(s, (0, 0))
#     visited = [[0]*n for _ in range(n)]

#     di = [-1, 0, 1, 0]
#     dj = [0, 1, 0, -1]

#     while s:
#         i, j = heapq.heappop(s)
#         for k in range(4):
#             ti = i + di[k]
#             tj = j + dj[k]
#             if 0 <= ti < n and 0 <= tj < n:
#                 temp =  visited[i][j] + data[ti][tj]
#                 if not visited[ti][tj] or visited[ti][tj] > temp:
#                     visited[ti][tj] = temp
#                     heapq.heappush(s, (ti, tj))
#     return visited[-1][-1]

# def find(i, j, path):
#     global minPath
#     di = [-1, 0, 1, 0]
#     dj = [0, 1, 0, -1]
#     s = []
#     s.append((i, j))
#     while s:
#         ti, tj = s.pop(0)
#         for k in range(4):
#             ci = ti + di[k]
#             cj = tj + dj[k]
#             if 0<= ci < len(data) and 0 <= cj < len(data) and not visited[ci][cj]:
#                 visited[ci][cj] = 1
#                 s.append((ci, cj))
#                 path += data[ci][cj]
#                 if ci == len(data)-1 and cj == len(data) -1:
#                     break
#     if minPath >= path:
#         minPath = path
#     return

# def find(i, j, path):
#     global minPath
#     if minPath <= path:
#         return
#     if i == len(data)-1 and j == len(data)-1:
#         if minPath >= path:
#             minPath = path
#         return
#     else:
#         di = [-1, 0, 1, 0]
#         dj = [0, 1, 0, -1]
#         for k in range(4):
#             ci = i + di[k]
#             cj = j + dj[k]
#             if 0 <= ci < len(data) and 0 <= cj < len(data) and not visited[ci][cj]:
#                 visited[ci][cj] = 1
#                 find(ci, cj, path+data[ci][cj])
#                 visited[ci][cj] = 0

# ------------------------------------------------------------

# t = int(input())

# def find(i, j, path):
#     global minPath
#     if minPath <= path:
#         return
#     if i == len(data)-1 and j == len(data)-1:
#         if minPath >= path:
#             minPath = path
#         return
#     else:
#         di = [-1, 0, 1, 0]
#         dj = [0, 1, 0, -1]
#         for k in range(4):
#             ci = i + di[k]
#             cj = j + dj[k]
#             if 0 <= ci < len(data) and 0 <= cj < len(data) and not visited[ci][cj]:
#                 visited[ci][cj] = 1
#                 find(ci, cj, path+data[ci][cj])
#                 visited[ci][cj] = 0


# for tc in range(1, t+1):
#     n = int(input())
#     data = [ list(map(int, input())) for _ in range(n) ]
#     visited = [ [0]*n for _ in range(n) ]
#     minPath = 1000000
#     find(0, 0, 0)
#     print(f'#{tc}', minPath)