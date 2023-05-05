def testCase(n):
    ans = 0
    for i in range(1, n+1):
        if i % 2 :
            ans += i
        else:
            ans -= i
    return ans


tc = int(input())
for t in range(tc):
    number = int(input())
    result = testCase(number)
    print('#{}'.format(t+1), result)