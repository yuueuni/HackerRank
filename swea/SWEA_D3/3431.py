T = int(input())

for tc in range(1, T+1):
    l, u, x = map(int, input().split())

    if x > u:
        ans = -1
    elif x >= l:
        ans = 0
    else:
        ans = l - x
    
    print('#{} {}'.format(tc, ans))