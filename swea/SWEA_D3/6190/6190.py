import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    multi = list(set( numbers[a]*numbers[b] for a in range(len(numbers)-1) for b in range(a+1, len(numbers))) )
    res = []
    for i in multi:
        check = True
        temp = str(i)
        if len(temp) == 1:
            check = False
        else:
            for j in range(len(temp)-1):
                if temp[j] > temp[j+1]:
                    check = False
                    break
        if check:
            res.append(int(temp))
    if len(res)>0:
        print(f'#{tc} {max(res)}')
    else:
        print(f'#{tc} -1')