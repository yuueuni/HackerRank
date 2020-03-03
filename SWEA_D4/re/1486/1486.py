import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\re\\1486\\input.txt')

T = int(input())

def test(data, b, arr):
    if not data:
        return arr
    d = data.pop(0)
    if sum(data)<b:
        return arr
    else:
        arr.append(sum(data))
    arr = test(data, b, arr)
    data.append(d)
    arr = test(data, b, arr)
    return arr
    


for tc in range(1, T+1):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))
    arr = []
    result = test(data, b, arr)
    print(f'#{tc} {result}')