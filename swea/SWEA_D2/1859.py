tc = int(input())

for t in range(tc):
    cnt = int(input())
    a = list(map(int, input().split()))
    res = 0
    i = cnt - 1

    while i > 0:
        j = i - 1
        c = 0
        while a[j] < a[i] and j >= 0:
            c += 1
            res -= a[j]
            j -= 1
        res += (c * a[i])
        i -= (c + 1)
    print('#{} {}'.format(t + 1, res))
