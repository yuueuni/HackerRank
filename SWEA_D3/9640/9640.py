import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D3\\re\\9640\\input.txt')

T = int(input())

def test(board, start, data):
    idx = start.pop()
    ci, cj = idx[0], idx[1]
    cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visit = [ [0]*len(board) for _ in range(len(board))]
    for d in data:
        if board[ci][cj] == d:
            visit[ci][cj] = 1
            cnt += 1
            continue
        for k in range(4):
            ti = ci + di[k]
            tj = cj + dj[k]
            if ti < 0 or tj < 0 or ti >= len(board) or tj >= len(board):
                continue
            if board[ti][tj] == d and visit[ti][tj] != 1:
                visit[ti][tj] = 1
                cnt += 1
                ci, cj = ti, tj
                break

    if cnt == len(data):
        return 1
    else:
        if start:
            return test(board, start, data)
        else:
            return 0


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    n = data.pop(0)
    m = int(input())
    board = []
    start = []
    for i in range(m):
        arr = list(map(int, input().split()))
        board.append(arr)
        if data[0] in arr:
            start.append([i, arr.index(data[0])])
    result = test(board, start, data)
    print(f'#{tc} {result}')