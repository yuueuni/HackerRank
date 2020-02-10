import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D3\\6057\\input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    dot = [ [] for _ in range(n+1) ]
    for _ in range(m):
        x, y = map(int, input().split())
        dot[x].append(y)
    
    cnt = 0
    for d in dot:
        if d:
            for i in d:
                for t in dot[i]:
                    if t in d:
                        cnt += 1

    print(f'#{tc} {cnt}')