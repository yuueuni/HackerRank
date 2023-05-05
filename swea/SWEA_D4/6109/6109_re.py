import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\6109\\input.txt')

T = int(input())


for tc in range(1, T+1):
    sn, k = input().split()
    n = int(sn)
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    rotations = {'left':0, 'down':1, 'right':2, 'up':3}
    r = rotations[k]
    
    # 회전
    for _ in range(r):
        board = list(zip(*board[::-1]))

    # 게임 진행
    result = [ [] for _ in range(n) ]
    for i in range(n):
        line = board[i]
        check = 0
        for j in range(n):
            if check != 0:
                check -= 1
                continue
            cur = line[j]
            if j+1 >= n:
                result[i].append(cur)
                break
            nex = line[j+1]
            if cur == 0:
                continue
            if nex == 0:
                if j+2 < n:
                    nex = line[j+2]
                    check += 1

            if cur == nex:
                result[i].append(cur*2)
                check += 1
            else:
                result[i].append(cur)

    # 빈자리 0 추가
    for res in result:
        temp = len(res)
        if temp != n:
            for _ in range(n-temp):
                res.append(0)
    
    # 회전
    for _ in range(4-r):
        result = list(zip(*result[::-1]))
    
    # 출력
    print(f'#{tc}')
    for re in result:
        print(*re)


