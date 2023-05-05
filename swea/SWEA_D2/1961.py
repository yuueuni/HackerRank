def rotation(n, matrix):
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][i] = matrix[n - i - 1][j]
    return ans


tc = int(input())
for t in range(tc):
    num = int(input())
    test_matrix = [ [0]*num for i in range(num)]
    for i in range(num):
        test_matrix[i] = list(map(int, input().split()))
    result = rotation(num, test_matrix)
    result2 = rotation(num, result)
    result3 = rotation(num, result2)
    print('#{}'.format(t+1))
    for k in range(num):
        print(''.join(str(x) for x in result[k]), ''.join(str(y) for y in result2[k]), ''.join(str(z) for z in result3[k]))