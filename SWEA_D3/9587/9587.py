import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(n, v, g):
    s = []
    s.append(n)
    visited[n] = 1
    while len(s) > 0:
        n = s.pop()
        #print(n, end=' ')
        if n == g:
            return 1
        for i in range(1, v+1):
            if adj[n][i] == 1 and visited[i] == 0:
                s.append(i)
                visited[i] = 1
    return 0


for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj = [ [0]*(v+1) for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    s, g = map(int, input().split())
    result = dfs(s, v, g)
    print(f'#{tc} {result}')
