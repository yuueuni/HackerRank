import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\1251\\input.txt')

import heapq

t = int(input())

def find(s):
    total = 0
    k[s] = 0
    heapq.heappush(hp, (k[s], 0))
	
    while hp:
        dist, u = heapq.heappop(hp)
        
        if visited[u]:
            continue

        visited[u] = 1
        total += d[p[u]][u] * tax
        
        for v in range(n):
            if not visited[v] and k[v] > d[u][v]:
                k[v] = d[u][v]
                p[v] = u
                heapq.heappush(hp, (k[v], v))
    
    return total

for tc in range(1, t+1):
    n = int(input())
    listX = list(map(int, input().split()))
    listY = list(map(int, input().split()))
    tax = float(input())
    
    INF = float('inf')
    k = [INF]*n
    visited = [0]*n
    p = list(range(n))
    
    hp = []
    d = [ [0]*n for _ in range(n) ]
    
    for i in range(n-1):
        for j in range(i+1, n):
            d[j][i] = d[i][j] = (listX[i] - listX[j])**2 + (listY[i] - listY[j])**2
    
    result = find(0)
    print(f'#{tc}', "%.f" %(result))