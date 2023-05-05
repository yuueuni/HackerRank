import sys

sys.stdin = open('c:\\tensor\\algorithm\\SWEA_D2\\4881\\input.txt')

T = int(input())

def find(datai):
    


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    result = find(data)
    print(f'#{tc} {result}')