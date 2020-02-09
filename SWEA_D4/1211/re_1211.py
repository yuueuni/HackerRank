import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1211\\input.txt')

def path(boardi, xi, yi):
    # 이동거리
    mv = 0
    while yi < 99:
        # 왼쪽
        if boardi[yi][xi-1]:
            # 왼쪽 길 있으면 쭉 진행
            while boardi[yi][xi-1]:
                xi -= 1
                mv += 1
            # 길 막혔으니까 밑으로 하나 내려감
            yi += 1
            mv += 1
        # 오른쪽
        elif boardi[yi][xi+1]:
            while boardi[yi][xi+1]:
                xi += 1
                mv += 1
            yi += 1
            mv += 1
        # 밑으로만 쭉쭉 내려감
        else:
            yi += 1
            mv += 1
    return mv



for _ in range(10):
    tc = int(input())
    # x 처음 끝 인덱스 범위 방지 위해 양쪽 끝에 의미없는 0 추가
    board = [ [0] + list(map(int, input().split())) + [0] for _ in range(100)]
    start_index = list(x for x in range(102) if board[0][x])
    
    result = {}
    for start in start_index:
        # key : 출발지, value:이동거리
        result[start] = path(board, start, 0)
    
    # 제일 짧은 거리
    mi = min(result.values())
    # 제일 짧은 거리인 출발지 리스트
    mx_idx = list(x-1 for x in result if result[x] == mi)
    print(f'#{tc}', max(mx_idx))