import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D2\\9476\\input.txt')

T = int(input())

def find(datai, ni, mi, ki, hi):
    cnt = 0
    for i in range(ni-2):
        for j in range(mi-2):
            around = []
            for y in range(i, i+3):
                temp = list(datai[y][x] for x in range(j, j+3))
                around.append(temp)
            landing = around[1].pop(1)
            max_a = max(max(a) for a in around)
            min_a = min(min(b) for b in around)
            if max_a - min_a <= ki:
                if landing >= min_a and (landing - min_a) <= hi:
                    cnt += 1
    return cnt


for tc in range(1, T+1):
    n, m, k, h = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    result = find(data, n, m, k, h)
    print(f'#{tc} {result}')