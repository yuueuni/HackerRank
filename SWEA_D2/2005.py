def pascal(number):
    ans =[ [1]*(n+1) for n in range(number) ]
    for i in range(1, number):
        for j in range(i):
            if j != 0:
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    return ans


tc = int(input())
for t in range(tc):
    n = int(input())
    result = pascal(n)
    print('#{}'.format(t+1))
    for line in result:
        print(' '.join(map(str, line)))