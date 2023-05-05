import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    tu = list(map(int, input().split()))
    c.sort(reverse=True)
    tu.sort(reverse=True)
    i = j = result = 0
    while i != len(c):
        if j >= len(tu):
            j = 0
            i += 1
        elif c[i] > tu[j]:
            j += 1
        else:
            result += c[i]
            c.pop(i)
            tu.pop(j)
    print(f'#{tc} {result}')