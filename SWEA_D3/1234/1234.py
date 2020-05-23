import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, data = map(str, input().split())
    i = 1
    result = data[0]
    while i != len(data):
        if not result:
            result += data[i]
        elif result[-1] == data[i]:
            result = result[:-1]
        else:
            result += data[i]
        i += 1
    print(f'#{tc} {result}')