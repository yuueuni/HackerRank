tc = int(input())
for t in range(tc):
    temp = list(map(int, input().split()))
    max_n = max(temp)
    min_n = min(temp)
    result = (sum(temp)-max_n-min_n)/(len(temp)-2)
    print('#{}'.format(t+1), '%0.0f  ' % result)