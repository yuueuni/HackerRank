import sys

sys.stdin = open('input.txt')

t = int(input())
 
for tc in range(1, t+1):
    n, a, b = map(int, input().split())
    minN = maxN = 0
    if n <= a + b:
        minN = (a+b)-n
    if a > b:
        maxN = b
    else:
        maxN = a
    print(f'#{tc} {maxN} {minN}')