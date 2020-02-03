def palindrome(n, m):
    cnt = 0
    for i in range(len(m)):
        for j in range(len(m)-n+1):
            temp = m[i][j:j+n]
            if temp == temp[::-1]:
                cnt += 1
    for i in range(len(m)):
        for j in range(len(m)-n+1):
            check = []
            for k in range(j, j+n):
                check.append(m[k][i])
            if check == check[::-1]:
                cnt += 1
    return cnt


for t in range(10):
    l = int(input())
    matrix = [[]*8 for _ in range(8)]
    for i in range(8):
        matrix[i] = list(input())
    result = palindrome(l, matrix)
    print('#{}'.format(t+1), result)