import sys

sys.stdin = open('input.txt')

T = int(input())

def find(node, n):
    global cnt
    cnt += 1
    if len(node[n]) == 1:
        find(node, node[n][0])
    elif len(node[n]) == 2:
        find(node, node[n][0])
        find(node, node[n][1])

for tc in range(1, T+1):
    e, n = map(int, input().split())
    node = [[] for _ in range(e+2)]
    data = list(map(int, input().split()))
    cnt = 0
    while data:
        p = data.pop(0)
        c = data.pop(0)
        node[p].append(c)
    find(node, n)
    print(f'#{tc}', cnt)