import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D4\\1258\\input.txt')

T = int(input())

def find(datai, ni):
    idx = []
    i = j = 0
    while i < ni:
        base = datai[i][j]
        if base:
            ti = tj = 1
            while datai[i][j+tj]:
                datai[i][j+tj] = 0
                tj += 1
            while datai[i+ti][j]:
                datai[i+ti][j] = 0
                ti += 1
            datai[i][j] = 0
            idx.append([ti, tj])
            j += tj
            if j> ni:
                i += ti+1
                j = 0
        else:
            j += 1
            if j > ni:
                j = 0
                i += 1
    return idx


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split()))+[0])
    result = find(data, n)
    s_result = []
    for r in result:
        temp = r[0]*r[1]
        s_result.append([temp, r[0], r[1]])
    s_result.sort()
    print(f'#{tc}', len(result), end =' ')
    for sr in s_result:
        stemp = sr[1:]
        print(*stemp, end=' ')
    print()
