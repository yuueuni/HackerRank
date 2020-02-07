import sys


sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1211\\input.txt')


def path(a, x, y, num):
    while y>0:
        if a[y][x-1]:
            while a[y][x-1]:
                x -= 1
                num += 1
            y -= 1
            num += 1
        elif a[y][x+1]:
            while a[y][x+1]:
                x += 1
                num += 1
            y -= 1
            num += 1
        else:
            y -= 1
            num += 1
    return x, num


for _ in range(10):
    tc = int(input())
    ladder = [ [0] + list(map(int, input().split())) +[0] for _ in range(100)]
    index = list(i for i in range(len(ladder[0])) if ladder[0][i])
    
    result = {}
    for i in index:
        x, y = i, 99
        idx, dis = path(ladder, x, y, 0)
        result[idx] = dis

    temp = min(result.values())
    answer = list(x-1 for x in result if result[x] == temp)
    #print('yes', sorted(result.items()))
    print(f'#{tc}', max(answer) )