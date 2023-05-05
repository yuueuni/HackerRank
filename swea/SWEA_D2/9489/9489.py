import sys

sys.stdin = open('input.txt')

T = int(input())


def find(datai, mi, ni):
    arch = []
    for i in range(ni):
        for j in range(mi):
            temp = datai[i][j]
            ci, cj = i, j
            cnt = 0
            if temp:
                cnt += 1
                if datai[ci+1][cj]:
                    while datai[ci+1][cj]:
                        ci += 1
                        cnt += 1
                elif datai[ci][cj+1]:
                    while datai[ci][cj+1]:
                        cj += 1
                        cnt += 1
                arch.append(cnt)
    return max(arch)


for tc in range(1, T+1):
    # n:세로 m:가로
    n, m = map(int, input().split())
    data = []
    # 오른쪽 끝과 마지막줄에 벽 추가
    # - out of index 방지
    for _ in range(n):
        data.append(list(map(int, input().split())) + [0])
    data.append([0]*(m+1))
    result = find(data, m, n)
    print(f'#{tc} {result}')