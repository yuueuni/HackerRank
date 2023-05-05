import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D2\\8810\\input.txt')

T = int(input())

def find(swpi, ni):
    result = []
    prep = cnt = sum_p = 0

    while swpi:
        cp = swpi.pop(0)
        if prep < cp:
            cnt += 1
            sum_p += cp
            if not swpi:
                result.append([cnt, sum_p])
        else:
            if cnt>1:
                result.append([cnt, sum_p])
                cnt = 1
                sum_p = cp
        prep = cp
    return result



for tc in range(1, T+1):
    n = int(input())
    swp = list(map(int, input().split()))
    result = find(swp, n)
    max_len = max_swp = 0
    for r in result:
        if max_len < r[0]:
            max_len = r[0]
            max_swp = r[1]
        if max_len == r[0]:
            if max_swp < r[1]:
                max_swp = r[1]
    print(f'#{tc}', len(result), max_swp)