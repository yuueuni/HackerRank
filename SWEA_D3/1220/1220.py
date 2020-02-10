import sys

sys.stdin = open('input.txt')

def mag(boardi):
    for _ in range(1):
        boardi = list(zip(*boardi[::-1]))
    cnt = i = j = 0
    for b in boardi:
        check = True
        if b.count(2) > 0:
            i = b.index(2)
            for j in range(i, 100):
                if b[j]==1 and check == True:
                    cnt += 1
                    check = False
                if b[j] == 2:
                    check = True
    return cnt


for tc in range(10):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    result = mag(board)
    print(f'#{tc+1} {result}')