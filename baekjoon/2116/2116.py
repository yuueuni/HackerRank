import sys

sys.stdin = open('input.txt')

n = int(input())

data = []
idx = [5, 3, 4, 1, 2, 0]

for _ in range(n):
    a, b, c, d, e, f = map(int, input().split())
    data.append([a, b, c, d, e, f])

final_result = []

for i in range(6):
    bottom_idx = i
    top_idx = idx[i]
    result = max(data[0][x] for x in range(6) if x != top_idx and x != bottom_idx)
    
    j = 1
    while j< n-1:
        top = data[j][top_idx]
        bottom = data[j][bottom_idx]
        
        result += max(data[j][x] for x in range(6) if x != top_idx and x != bottom_idx)
        
        j += 1
        bottom_idx = data[j].index(top)
        top_idx = idx[bottom_idx]
    
    result += max(data[j][x] for x in range(6) if x != top_idx and x != bottom_idx)
    final_result.append(result)

print(final_result)