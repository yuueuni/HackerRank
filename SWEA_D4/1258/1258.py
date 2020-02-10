import sys

sys.stdin = open('c:\\Users\\multicampus\\Desktop\\vscode\\algorithm\\SWEA_D4\\1258\\input.txt')

T = int(input())

def find(datai, ni):
    idx = []
    for i in range(ni):
        start_idx = list(x for x in range(ni) if datai[i][x] != 0)






for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split()))+[0])
    result = find(data, n)
    #print(f'#{tc}', len(result),  *result.values())
    print(f'#{tc} {result}')