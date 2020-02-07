import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1211\\input.txt')

def path(boardi, xi, yi):
    # 이동거리
    mv = 0
    while yi < 99:
        # 왼쪽
        if boardi[yi][xi-1]:
            while boardi[yi][xi-1]:
                xi -= 1
                mv += 1
            yi += 1
            mv += 1
        # 오른쪽
        elif boardi[yi][xi+1]:
            while boardi[yi][xi+1]:
                xi += 1
                mv += 1
            yi += 1
            mv += 1
        else:
            yi += 1
            mv += 1
    return mv



for _ in range(10):
    tc = int(input())
    board = [ [0] + list(map(int, input().split())) + [0] for _ in range(100)]
    start_index = list(x for x in range(102) if board[0][x])
    
    result = {}
    for start in start_index:
        result[start] = path(board, start, 0)
    
    mi = min(result.values())
    mx_idx = list(x-1 for x in result if result[x] == mi)
    
    #print('no', sorted(result.items()))
    print(f'#{tc}', max(mx_idx))