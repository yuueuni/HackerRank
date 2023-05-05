import sys

sys.stdin = open('input.txt')

T = int(input())

def find(datai, ni):
    center = ni // 2
    csum = check = 0
    for i in range(ni):
        for j in range(check, ni-check):
            if i == center and j == center:
                return csum
            csum += datai[i][j]
        check += 1


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    result = []
    for i in range(4):
        for _ in range(i):
            data = list(zip(*data[::-1]))
        temp = find(data, n)
        result.append(temp)
    print(f'#{tc}', max(result)-min(result))