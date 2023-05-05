import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1210\\input.txt')


def find(boardi, b):
    a = 100
    while a>0:
        if boardi[a][b+1]:
            while boardi[a][b+1]:
                b += 1
            a -= 1
        elif boardi[a][b-1]:
            while boardi[a][b-1]:
                b -= 1
            a -= 1
        else:
            a -= 1
    return b-1


for tc in range(10):
    tc = int(input())
    board = [ [0 for _ in range(102) ] ]
    for _ in range(100):
        board.append([0]+list(map(int, input().split()))+[0])
    finish = board[-1].index(2)
    result = find(board, int(finish))
    print(f'#{tc} {result}')
