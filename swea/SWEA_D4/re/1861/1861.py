import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\re\\1861\\input.txt')

T = int(input())

def test(data, n):
    # 방안의 숫자 나열한 리스트
    check = [0]*(n*n+1)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ti = i + di[k]
                tj = j + dj[k]
                # +1 만 고려
                if 0<=ti<n and 0<=tj<n and data[i][j] + 1 == data[ti][tj]:
                    # check 리스트 1입력
                    check[data[i][j]] = 1
    
    max_cnt = cnt = idx = 0
    # 연속된 1의 숫자 비교 => 같을 경우 작은 숫자 우선이므로 큰 숫자부터 탐색
    for c in range(n*n, -1, -1):
        if check[c]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                idx = c+1
            cnt = 0
    # idx 시작할 숫자, max_cnt 길이
    return idx, max_cnt+1


for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    id, result = test(data, n)
    print(f'#{tc} {id} {result}')
