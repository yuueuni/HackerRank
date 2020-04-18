import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input()))
    count = 0
    check = [0 for _ in range(len(data))]
    for i in range(len(check)):
        if count % 2:
            temp = int(not check[i])
        else:
            temp = check[i]
        if temp != data[i]:
            count += 1
    print(f'#{tc} {count}')