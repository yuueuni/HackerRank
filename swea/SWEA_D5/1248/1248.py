t = int(input())

def order(n):
    global depth
    if n != 0:
        depth += 1
        order(node[n][0])
        order(node[n][1])

def find(current, parents):
    if current != 0:
        tn = node[current][2]
        if tn in parents:
            return tn
        parents.append(tn)
        return find(tn, parents)
    else:
        return parents

for tc in range(1, t+1):
    v, e, findA, findB = map(int, input().split())
    data = list(map(int, input().split()))
    node = [ [0]*3 for _ in range(v+1) ]
    depth = 0
    for i in range(e):
        p = data[i * 2]
        c = data[i * 2 + 1]
        if not node[i][0]:
            node[p][0] = c
        else:
            node[p][1] = c
        node[c][2] = p
    temp = []
    pA = find(findA, temp)
    pB = find(findB, pA)
    order(pB)
    print(f'#{tc}', pB, depth)