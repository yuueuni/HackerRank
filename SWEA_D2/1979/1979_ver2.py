import sys

sys.stdin = open('C:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D2\\1979\\input.txt')

T = int(input())
# 1:white(blank) // 0 :Black
for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = list([int(x) for x in input().split()] for _ in range(n))
    res = cnt_h = cnt_v = 0
    for i in range(n):
        for j in range(n):
            hor = board[i][j]
            ver = board[j][i]
            if hor:
                cnt_h += 1
            else:
                if cnt_h == k:
                    res += 1
                cnt_h = 0
            if ver:
                cnt_v += 1
            else:
                if cnt_v == k:
                    res += 1
                cnt_v = 0
        if cnt_h == k:
            res += 1
        cnt_h = 0
        if cnt_v == k:
            res += 1
        cnt_v = 0
    print(f'#{tc} {res}')