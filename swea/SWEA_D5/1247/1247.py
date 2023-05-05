import sys

sys.stdin = open('input.txt')

t = int(input())

def find(count, d, visited, start):
    global n
    global minD
    if count == n:
        d += distance[start][n+1]
        if minD >= d:
            minD = d
        return
    else:
        for i in range(1, n+1):
            if not visited[i-1] and start != i:
                current = distance[start][i]
                visited[i-1] = 1
                find(count+1, d+current, visited, i)
                visited[i-1] = 0

for tc in range(1, t+1):
    n = int(input())
    temp = list(map(int, input().split()))
    data = temp[:2] + temp[4:] + temp[2:4]
    distance = list([0]*(n+2) for _ in range(n+2))
    v = [0] * n
    minD = float('inf')
    for i in range(0, len(data)-1, 2):
        for j in range(0, len(data)-1, 2):
            if i != j:
                tx = abs(data[i]-data[j])
                ty = abs(data[i+1]-data[j+1])
                distance[i//2][j//2] = tx + ty
    find(0, 0, v, 0)
    print(f'#{tc}', minD)