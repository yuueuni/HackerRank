def test(stM, stD, fiM, fiD):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if stM == fiM:
        ans = fiD - stD +1
    else:
        ans = fiD - stD +1
        for k in range(stM-1, fiM-1):
            ans += m[k]
    return ans


tc = int(input())
for t in range(tc):
    stM, stD, fiM, fiD = map(int, input().split(' '))
    result = test(stM, stD, fiM, fiD)
    print('#{}'.format(t+1), result)