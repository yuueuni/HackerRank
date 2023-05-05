import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D2\\8706\\input.txt')


T = int(input())

def move(carroti, ni, mi):
    cart = mv = 0
    for i in range(ni):
        cart += carroti[i]
        if i == (ni-1):
            mv += (i+1)*2
        if cart >= mi:
            cart -= mi
            mv += (i+1)*2
            if cart >= mi:
                cart -= mi
                mv += (i+1)*2
    return mv


for tc in range(1, T+1):
    n, m = map(int, input().split())
    carrot = list(map(int, input().split()))
    result = move(carrot, n, m)
    print(f'#{tc} {result}')