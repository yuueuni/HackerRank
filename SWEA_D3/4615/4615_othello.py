import sys

sys.stdin = open('input.txt')

T = int(input())

# 1:B 2:W
def othello(n, matrix, a, b, color):
    # 위부터 시계방향순
    dy = [-1, -1, 0, 1, 1, 1, 0, -1] # b = j
    dx = [0, 1, 1, 1, 0, -1, -1, -1] # a = i
    
    # 8방향 확인
    for i in range(8):

        # 변경되는 인덱스 리스트
        chg_idx = []
        # 변경 기준 인덱스 /= 같은 컬러인 기준 인덱스
        idx = []

        ta = a + dx[i]
        tb = b + dy[i]
        # 8방향 변경 ---1
        temp = matrix[tb][ta]
        # 1과 같은 방향으로 인덱스 변경해가며 같은색이나 0(빈칸) 확인
        while temp != 0:
            # 다른 컬러: 변경해야 할 인덱스에 추가
            if temp != c:
                chg_idx.append([ta, tb])
            # 같은 컬러 나와야 변경가능하므로 변경기준 인덱스 확인
            elif temp == c:
                idx.append([ta, tb])
                break
            # 1과 같은방향
            ta = ta + dx[i]
            tb = tb + dy[i]
            temp = matrix[tb][ta]
        # 같은컬러 없으면 변경 X
        # - 유무 확인
        if idx:
            # 변경할 인덱스 리스트로 색 변경
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
    # 각 라인별 색 카운트
    black = sum(bla.count(1) for bla in board)
    white = sum(wh.count(2) for wh in board)
    print(f'#{tc}',black, white)
