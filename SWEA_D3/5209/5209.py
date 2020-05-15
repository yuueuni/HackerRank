import sys

sys.stdin = open('input.txt')

t = int(input())

def find(data, i, tsum):
    global result
    if tsum < result:
        if i < len(data):
            for j in range(len(data)):
                if not visited[j]:
                    visited[j] = 1
                    find(data, i+1, tsum+data[i][j])
                    visited[j] = 0
        else:
            result = tsum

for tc in range(1, t+1):
    v = int(input())
    data = [list(map(int, input().split())) for _ in range(v) ]
    visited = [0]*len(data)
    result = 10000
    find(data, 0, 0)
    print(f'#{tc} {result}')