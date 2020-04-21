import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    while 1:
        if cnt == 6:
            cnt = 1
        temp = data.pop(0)
        temp -= cnt
        cnt += 1
        if temp <= 0:
            data.append(0)
            break
        data.append(temp)
    print(f'#{tc}' ,*data)