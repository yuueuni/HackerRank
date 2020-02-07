import sys

sys.stdin = open('input.txt')


def test(n, k, blocks):
    cnt = 0
    # 가로 i 세로 j
    for i in range(n):
        check = check2 = 0
        for j in range(n):
            # vertical
            temp2 = blocks[j][i]
            # horizon
            temp = blocks[i][j]
            if temp == 1:
                check += 1
            elif temp == 0:
                if check == k:
                    cnt += 1
                    check = 0
                else:
                    check = 0
        if check == k:
            cnt += 1
        for j in range(n):
            # vertical
            temp2 = blocks[j][i]
            if temp2 == 1:
                check2 += 1
            elif temp2 == 0:
                if check2 == k:
                    cnt += 1
                    check2 = 0
                else:
                    check2 = 0
        if check2 == k:
            cnt += 1
    return cnt


tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    block = []
    for l in range(N):
        tes = list(map(int, input().split()))
        block.append(tes)
    result = test(N, K, block)
    print('#{}'.format(t + 1), result)