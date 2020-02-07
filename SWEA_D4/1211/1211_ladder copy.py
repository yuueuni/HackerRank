import sys


sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1211\\input.txt')

# 양쪽 확인
def leftright():
    while 1:
        temp += 1
        if ladder[fix+1][temp]:
            return right, temp
        elif ladder[fix-1][temp]:
            return left, temp


# 가는길 확인
def down():
    if right:
        while ladder[temp][fix]:
            temp += 1
        return temp-1
    else:
        while ladder[temp][fix]:
            temp -= 1
        return temp+1


for _ in range(10):
    n = int(input())
    ladder = [ [0] + list(map(int, input().split())) +[0] for _ in range(100)]
    i = j = 0
    ro = 1
    # [거리, 출발점]
    temp = []
    dis = start = 0
    while i != 99:
        if ro:
            if ladder[i][j+1] == 0:
                i -= 1
                ro = 0
                dis += i
            elif ladder[i][j-1] == 0:
                i -= 1
                ro = 0
                dis += i
            else:
                i += 1
        else:
            if ladder[i][j] == 0:
                j -= 1
                ro = 1
                dis += j
            else:
                j += 1
    temp.append([dis, start])
    print(f'#{n} {temp}')