import sys

sys.stdin = open('input.txt')


def recursive(n, m, result):
    if m:
        m -= 1
        result *= n
        return recursive(n, m, result)
    else:
        return result


for _ in range(10):
    T = int(input())
    n, m = map(int, input().split())
    result = recursive(n, m, 1)
    print(f'#{T} {result}')