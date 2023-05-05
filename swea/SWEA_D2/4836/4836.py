import sys

sys.stdin = open('input.txt')

T = int(input())

def paint(boardi, ri1, ci1, ri2, ci2, colori):
    for i in range(ri1, ri2+1):
        for j in range(ci1, ci2+1):
            boardi[i][j] += colori
    return boardi



for tc in range(1, T+1):
    n = int(input())
    board = [ [0 for _ in range(10)] for _ in range(10) ]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        board = paint(board, r1, c1, r2, c2, color)
    cnt = sum(b.count(3) for b in board)
    print(f'#{tc} {cnt}')