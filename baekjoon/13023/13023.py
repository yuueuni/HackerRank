import sys

v, edge = map(int, input().split())
m = [ [0]*v for _ in range(v)]
g = [ [] for _ in range(v)]
# {node: [e1, e2]}
k = []

for _ in range(edge):
    f, t = map(int, input().split())
    # 1. 인접행렬
    # [[]]
    m[f][t] = m[t][f] = 1

    # 2. 인접 리스트
    # {f: [t1, t2]}
    g[f].append(t)
    g[t].append(f)

    # 3. edge리스트
    k.append([f, t])
    k.append([t, f])

for i in range(len(k)):
    for j in range(len(k)):
        a, b = k[i]
        c, d = k[j]

        if a == b or a == c or a == d or b ==c or b == d or c == d:
            continue
        if not m[b][c]:
            continue
        for e in g[d]:
            if e == a or e == b or e == c or e == d:
                continue
            print(1)
            sys.exit(0)
else:
    print(0)

# -> 출력
#print(m)
#print(a)