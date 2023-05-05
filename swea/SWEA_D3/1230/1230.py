import sys

sys.stdin = open('input.txt')

def solve(data, test):
    while test:
        temp = test.pop(0)
        t = int(test.pop(0))
        #idx = data.index(t)
        if temp == 'I':
            cnt = int(test.pop(0))
            for _ in range(cnt):
                data.insert(t, test.pop(0))
                t += 1
        elif temp == 'D':
            cnt = int(test.pop(0))
            for _ in range(cnt):
                data.pop(t)
        else:
            for _ in range(t):
                data.append(test.pop(0))
    return data[:10]

for tc in range(1, 11):
    n = int(input())
    data = list(map(str, input().split()))
    m = int(input())
    test = list(map(str, input().split()))
    result = solve(data, test)
    print(f'#{tc}', *result)