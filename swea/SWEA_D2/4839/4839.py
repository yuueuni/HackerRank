import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D2\\4839\\input.txt')

T = int(input())

def find(pi, ab):
    c = pi//2
    cnt = 1
    start = 1
    end = pi
    while c != ab:
        if ab > c:
            start = c
        else:
            end = c
        c = (start+end)//2
        cnt += 1
    return cnt


for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    result_a = find(p, a)
    result_b = find(p, b)
    
    if result_a > result_b:
        result = 'B'
    elif result_a < result_b:
        result = 'A'
    else:
        result = 0
    
    print(f'#{tc} {result}')