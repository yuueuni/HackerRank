import sys

sys.stdin = open('input.txt')

T = int(input())

def base_board():
    temp = 1
    first = []
    board = []
    for i in range(300):
        temp += i
        first.append(temp)
    for f in range(300):
        line = [first[f]]
        t = 0
        for j in range(len(first)-1):
            if j == 0:
                t = f+2
            else:
                t += 1
            line.append(line[-1]+t)
        board.append(line)
    return board


for tc in range(1, T+1):
    p, q = map(int, input().split())
    base = base_board()
    for i in range(len(base)):
        for j in range(len(base)):
            if base[i][j] == p:
                px = i
                py = j
            if base[i][j] == q:
                qx = i
                qy = j
    temp_a = px+qx
    temp_b = py+qy
    result = base[temp_a+1][temp_b+1]
    print(f'#{tc} {result}')