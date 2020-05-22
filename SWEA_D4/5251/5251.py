
t = int(input())

for tc in range(1, t+1):
    n, e = map(int, input().split())
    n += 1
    adj = {i : [] for i in range(n)}
    for i in range(e):
        s, e, c = map(int, input().split())
        adj[s].append((e, c))

    INF = float('inf')
    d = [INF] * n
    p = [-1] * n
    visited = [False] * n
    d[0] = 0

    for _ in range(n):
        mindex = -1
        m = INF
        for i in range(n):
            if not visited[i] and d[i] < m:
                m = d[i]
                mindex = i
        visited[mindex] = True
        for v, val in adj[mindex]:
            if not visited[v] and d[mindex] + val < d[v]:
                d[v] = d[mindex] + val
                p[v] = mindex
    print(f'#{tc} {d[-1]}')