from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    line = [ [] for _ in range(n+1) ]
    for i in range(0, len(data)-1, 2):
        line[data[i]].append(data[i+1])
        line[data[i+1]].append(data[i])
    
    cnt = 0
    visit = []
    queue = deque()

    for j in range(1, n+1):
        if j not in visit and line[j] not in visit:
            cnt += 1
            queue.append(j)
            while queue:
                node = queue.popleft()
                if node not in visit:
                    visit.append(node)
                    queue.extend(line[node])
    print(f'#{tc} {cnt}')