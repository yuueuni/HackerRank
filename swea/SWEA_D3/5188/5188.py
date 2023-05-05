import sys

sys.stdin = open('input.txt')

T = int(input())

def find(i, j, sumn):
    temp = data[i][j]
    sumn += temp
    global result
    if sumn < result:
    	if i == (len(data)-1) and j == (len(data)-1):
        	result = sumn
    	else:
            if i != (len(data)-1):
                find(i+1, j, sumn)
            if j != (len(data)-1):
                find(i, j+1, sumn)
    else:
        pass

for tc in range(1, T+1):
    n = int(input())
    result = 10000000
    data = [list(map(int, input().split())) for _ in range(n)]
    find(0, 0, 0)
    print(f'#{tc} {result}')