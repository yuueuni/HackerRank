import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    dot = [[] for _ in range(v)]
    for i in range(0, len(data), 2):
        dot[data[i]].append(data[i+1])
    print(dot)

