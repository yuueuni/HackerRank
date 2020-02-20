import sys

sys.stdin = open('c:\\tensor\\algorithm\\SWEA_D2\\4880\\input.txt')

T = int(input())


def find(group):
    # group [ idx, card ]
    if len(group) > 2:
        temp = (len(group)+1)//2
        ta = find(group[:temp])
        tb = find(group[temp:])
    elif len(group) == 1:
        ta = tb = group[0]
    else:
        ta = group[0]
        tb = group[1]
    # 1 : 가위, 2 : 바위 , 3 : 보
    # - 1 < 2, 2 < 3, 3 < 1
    i = ta[1]
    j = tb[1]
    if i == j:
        winner = ta
    elif (i+1-j)%3 == 0:
        winner = tb
    else:
        winner = ta
    return winner


for tc in range(1, T+1):
    n = int(input())
    idx = list(x for x in range(1, n+1))
    card = list(map(int, input().split()))
    data = list(zip(idx, card))
    result = find(data)
    print(f'#{tc} {result[0]}')