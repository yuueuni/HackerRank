# import sys

# sys.stdin = open('input.txt')

T = int(input())

def test(board):
    return 1


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    n = data.pop(0)
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(m) ]
    result = test(board)
    print(f'#{tc} {result}')