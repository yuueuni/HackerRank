import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num = list(input())
    cnt = 0
    result = []
    for m in num:
        if m == '1':
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)
    print(f'#{tc}', max(result))