
import sys

sys.stdin = open('input.txt')

T = int(input())


# ------------------- 기본 반복문 버전 -----------------------------

def f(n, k):
    global minV
    if n == k: # 순열 1개 완성
        s = 0
        for i in range(k):
            s += arr[i][p[i]] # p[i] i번 행에서 선택한 열 번호
        if minV > s:
            minV = s

    else:
        for i in range(k): # used를 왼쪽부터 탐색(사용할 수 있는 숫자 탐색)
            if u[i] == 0: # 이미 사용한 숫자가 아니면
                u[i] = 1
                p[n] = i
                f(n+1, k) # 다음 자리를 결정하러 이동
                u[i] = 0

# ------------------- 백트래킹 버전 -----------------------------

def f(n, k, s):
    global minV
    cnt += 1
    if n == k:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1
                f(n+1, k, s + arr[n][i])
                u[i] = 0

# ??????????????


for tc in range(1, T+1):
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n)]
    p = [0]*n
    u = [0]*n
    minV = 10*n
    f(0, n)
    print(f'#{tc} {minV}')