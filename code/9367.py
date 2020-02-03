tc = int(input())
for t in range(tc):
    n = int(input())
    carrot = list(map(int, input().split()))
    cnt = 1
    res = [0]
    for i in range(1, len(carrot)):
        temp = carrot[i-1] - carrot[i]
        if temp < 0:
            cnt += 1
        elif temp >= 0:
            res.append(cnt)
            cnt = 1
    if cnt < max(res):
        cnt = max(res)
    print('#{}'.format(t+1), cnt)
