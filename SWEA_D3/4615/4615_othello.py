import sys

sys.stdin = open('input.txt')

T = int(input())

# 1:B 2:W
def othello(n, matrix, a, b, color):
    # 위부터 시계방향순
    dy = [-1, -1, 0, 1, 1, 1, 0, -1] # b = j
    dx = [0, 1, 1, 1, 0, -1, -1, -1] # a = i
    for i in range(8):
        chg_idx = []
        idx = []
        ta = a + dx[i]
        tb = b + dy[i]
        temp = matrix[tb][ta]
        while temp != 0:
            if temp != c:
                chg_idx.append([ta, tb])
            elif temp == c:
                idx.append([ta, tb])
                break
            ta = ta + dx[i]
            tb = tb + dy[i]
            temp = matrix[tb][ta]
        if idx:
            for j in chg_idx:
                matrix[j[1]][j[0]] = c
    return matrix
    
    


for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 게임판 + 벽 추가. index-1 안하고 바로 사용
    board = [ [0]*(n+2) for _ in range(n+2)]
    #기본 배치
    board[n//2][n//2] = 2
    board[(n//2)+1][(n//2)+1] = 2
    board[n//2][(n//2)+1] = 1
    board[(n//2)+1][n//2] = 1
    # 게임 진행
    for _ in range(m):
        i, j, c = map(int, input().split())
        board[j][i] = c
        board = othello(n, board, i, j, c)
    black = sum(bla.count(1) for bla in board)
    white = sum(wh.count(2) for wh in board)
    print(f'#{tc}',black, white)
