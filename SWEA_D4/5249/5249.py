t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    v += 1
    adj = [ [0] * v for _ in range(v) ]
    for _ in range(e):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c
    
    INF = float('inf')
    key = [INF] * v
    p = [-1] * v
    mst = [False] * v
    
    key[0] = 0
    cnt = result = 0
    while cnt < v:
        m = INF
        u = -1
        for i in range(v):
            if not mst[i] and key[i] < m:
                m = key[i]
                u = i
        mst[u] = True
        result += m
        cnt += 1
        for w in range(v):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u
    print(f'#{tc} {result}')