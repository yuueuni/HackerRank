import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(input()))
    result = check = 0
    for i in range(n):
        temp = data[i]
        c = n//2
        if i > c:
            check += 2
        for j in range(c-i+check, c+i+1-check):
            result += int(temp[j])
    print(f'#{tc} {result}')