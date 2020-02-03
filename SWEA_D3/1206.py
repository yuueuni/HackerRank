for t in range(10):
    tc = int(input())
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(b) - 1):
        temp = b[i - 2:i + 3]
        if max(temp) == temp[2]:
            base = temp.pop(2)
            check = base - max(temp)
            cnt += check
    print('#{}'.format(t + 1), cnt)

