def bake(waiting, second, making):
    ans = 'Possible'
    cnt = 0
    while waiting:
        temp = waiting.pop(0)
        check = temp//second
        if check  == 0 or (check*making)+cnt <1:
            ans = 'Impossible'
            break
        cnt -= 1
    return ans


tc = int(input())
for t in range(tc):
    #n명 m초에 k개
    n, m, k = map(int, input().split())
    wait = list(map(int, input().split()))
    result = bake(sorted(wait), m, k)
    print('#{}'.format(t+1), result)
