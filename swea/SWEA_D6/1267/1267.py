import sys

sys.stdin = open('input.txt')

## BFS 이용 > 작업 순서 역순으로 구하기.

T = 10

def bfs(graph, start_node):
    visit = {}
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])
    
    return visit


for tc in range(1, T+1):
    v, e = map(int, input().split())
    data = list(input().split())
    data_odd = list(int(data[x]) for x in range(len(data)) if x%2)
    start = list(x for x in range(1, v+1) if x not in data_odd)
    dot = {}
    for i in range(0, len(data), 2):
        idx = int(data[i])
        if idx in dot:
            dot[idx].append(list(map(int, data[i+1])))
        else:
            dot[idx] = list(map(int, data[i+1]))
    #print(f'#{tc}', dot)
    result = bfs(dot, start[0])
    print(f'#{tc}', *result)
    
