import sys

#sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\6109\\input.txt')

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
        line = list(x for x in board[i])
        check = 0
        jn = 1
        for j in range(n):
            if jn != 1:
                jn -= 1
                continue
            cur = line[j]
            if j+jn >= n:
                result[i].append(cur)
                break
            nex = line[j+jn]
            if cur == 0:
                continue
            if nex == 0:
                while nex == 0:
                    jn += 1
                    if j+jn >= n:
                        result[i].append(cur)
                        break
                    nex = line[j+jn]
            if j+jn >= n:
                break

            if cur == nex:
                result[i].append(cur*2)
                line[j+jn] = 0
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


