tc = int(input())
for t in range(tc):
    m = int(input())
    scores = list(map(int, input().split()))
    cnt = [0]*100
    for i in range(100, 0, -1):
        cnt[100-i] = scores.count(i)
    result = cnt.index(max(cnt))
    print('#{}'.format(m), 100-result)