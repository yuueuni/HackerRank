for _ in range(4):

    ar1, ac1, ar2, ac2, br1, bc1, br2, bc2 = map(int, input().split())

    base = [ar1, ac1, ar2, ac2]
    test = [br1, bc1, br2, bc2]

    bw = base[2]-base[1]
    bh = base[3]-base[0]

    cnt = 0
    for b in base:
        if b in test:
            cnt += 1

    if ar1 < br1:
        bw *= (-1)
    if ac1 < bc1 :
        bh *= (-1)

    if cnt == 2:
        ans = 'c'
    elif cnt == 1:
        ans = 'b'
    elif br1-bw > ar1 and bc1 - bh > ac1:
        ans = 'd'
    else:
        ans = 'a'

    print(ans)