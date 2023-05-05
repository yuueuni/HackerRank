import sys

sys.stdin = open('input.txt')


T = int(input())

def find(node, s, g):
    q = []
    visited = [0]*(len(node)+1)
    distance = [0]*(len(node)+1)
    q.append(s)
    visited[s] = 1
    while q:
        start = q.pop(0)
        for nx in range(1, v+1):
            if node[start][nx] and not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                distance[nx] = distance[start] + 1
                if nx == g:
                    return distance[nx]
    return 0


for tc in range(1, T+1):
    v, e = map(int, input().split())
    node = [ [0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        n1, n2 = map(int, input().split())
        node[n1][n2] = 1
        node[n2][n1] = 1
    s, g = map(int, input().split())
    result = find(node, s, g)
    print(f'#{tc} {result}')