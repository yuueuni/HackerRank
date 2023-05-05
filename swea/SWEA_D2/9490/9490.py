import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D2\\9490\\input.txt')

T = int(input())

def pang(boardi, mi, ni):
    dm = [0, 1, 0, -1]
    dn = [-1, 0, 1, 0]

    pang_list = []

    for cn in range(ni):
        for cm in range(mi):
            pb = 0
            flower = boardi[cn][cm]
            pb += flower
            for i in range(4):
                temp = flower
                tm, tn = cm, cn
                while temp:
                    tm += dm[i]
                    tn += dn[i]
                    if tm < 0 or tm >= mi or tn < 0 or tn >= ni:
                        break
                    nex = boardi[tn][tm]
                    pb += nex
                    temp -= 1
            pang_list.append(pb)
    return max(pang_list)


for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    result = pang(board, m, n)
    print(f'#{tc} {result}')