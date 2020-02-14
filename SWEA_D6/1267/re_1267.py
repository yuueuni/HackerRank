import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    v, e = map(int, input().split())
    data = []
    for _ in range(e):
        data.append(list(map(int, input().split())))
    print(f'{tc}')
    print(data)