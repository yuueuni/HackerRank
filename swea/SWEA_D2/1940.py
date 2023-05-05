def test(a, v):
    if a[0] == 0:
        return v
    elif a[0] == 1:
        v += a[1]
    elif a[0] == 2:
        v -= a[1]
    if v < 0:
        v = 0
    return v


tc = int(input())
for t in range(tc):
    result = distance = 0
    N = int(input())
    for n in range(N):
        vc = list(map(int, input().split()))
        result = test(vc, result)
        distance += result
    print('#{}'.format(t+1), distance)