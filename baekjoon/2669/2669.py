import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\baekjoon\\2669\\input.txt')

board = [ [0 for _ in range(100)] for _ in range(100) ]

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] = 1

result = 0
for b in board:
    result += b.count(1)

print(result)