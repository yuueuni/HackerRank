def water(p, q, r, w, s):
    chargeA = w * p
    if w <= r:
        chargeB = q
    else:
        chargeB = q + (w-r)*s
    if chargeA < chargeB:
        ans = chargeA
    else:
        ans = chargeB
    return ans


tc = int(input())
for t in range(tc):
    P, Q, R, S, W = map(int, (input().split(' ')))
    result = water(P, Q, R, W, S)
    print('#{}'.format(t+1), result)