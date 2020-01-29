def howkill(h, s, matrix):
    ans = []
    for i in range(h-s+1):
        for j in range(h-s+1):
            temp = 0
            for y in range(s):
                for x in range(s):
                    temp += matrix[i+y][j+x]
            ans.append(temp)
    return max(ans)


tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    board = [ [0] * N for i in range(N) ]
    for l in range(N):
        board[l] = list(map(int, input().split()))
    result = howkill(N, M, board)
    print('#{}'.format(t+1), result)