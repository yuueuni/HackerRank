
def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    print(v, end='-')

    while stack:
        for v in G[v]:
            if not visited[w]:
                stack.append(w)
                v = w
                visited[w] = 1
                print(v, end='-')
                break
        else:
            if p == v:
                