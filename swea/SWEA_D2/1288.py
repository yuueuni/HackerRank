def cntSheep(n):
    cnt_num = []
    i = 1
    while len(cnt_num)<10:
        temp = n * i
        cnt_num += list(str(temp))
        cnt_num = list(set(cnt_num))
        i += 1
    ans = temp
    return ans


tc = int(input())
for t in range(tc):
    number = int(input())
    result = cntSheep(number)
    print('#{}'.format(t+1), result)