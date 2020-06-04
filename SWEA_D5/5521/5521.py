import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D5\\5521\\input.txt')

import heapq

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    friend = [ [0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a][b] = 1
        friend[b][a] = 1
    
    s = []
    heapq.heappush(s, 1)

    visited = [0]*(n+1)
    visited[1] = 1

    cnt = 0

    while s:
        c = heapq.heappop(s)
        if visited[c] < 3:
            for i in range(1, n+1):
                if friend[c][i] == 1 and not visited[i]:
                    heapq.heappush(s, i)
                    visited[i] = visited[c] + 1
                    cnt += 1
    print(f'#{tc} {cnt}')

# ----------------------------------------------------------------
# t = int(input())

# def find(n):
#     q = [1]
#     v = [0]*(n+1)
#     v[1] = 1
#     cnt = 0
#     while q:
#         t = q.pop(0)
#         cnt += 1
#         if v[t] <= 2:
#             for i in range(1, n+1):
#                 if adj[t][i] == 1 and v[i] == 0:
#                     q.append(i)
#                     v[i] = v[t]+1
#     return cnt - 1

# for tc in range(1, t+1):
#     n, m = map(int, input().split())
#     adj = [ [0]*(n+1) for _ in range(n+1) ]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         adj[a][b] = 1
#         adj[b][a] = 1
#     result = find(n)
#     print(f'#{tc} {result}')