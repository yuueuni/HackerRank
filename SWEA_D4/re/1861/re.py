import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\re\\1861\\input.txt')


T = int(input())

def test(data, n):
    check = [0]*(n*n+1)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(4):
                ti = i + di[k]
                tj = j + dj[k]
                if data[i][j] + 1 == data[ti][tj]:
                    check[data[i][j]] = 1
    max_cnt = cnt = idx = 0
    for c in range(n*n, -1, -1):
        if check[c]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                idx = c+1
            cnt = 0
    return idx, max_cnt+1


for tc in range(1, T+1):
    n = int(input())
    data = [[-1]*(n+2)]
    for _ in range(n):
        data.append([-1]+list(map(int, input().split()))+[-1])
    data.append([-1]*(n+2))
    id, result = test(data, n)
    print(f'#{tc} {id} {result}')