n = int(input())

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
idx = 1
for i in range(1, n+1):
    tc = input()
    year = tc[:4]
    month = tc[4:6]
    day = tc[-2:]
    if int(month) == 0 or int(month) > 12:
        print('#{}'.format(idx), '-1')
        idx += 1
    elif int(day) > date[int(month)-1]:
        print('#{}'.format(idx), '-1')
        idx += 1
    else:
        print('#{}'.format(idx), '{}/{}/{}'.format(year, month, day))
        idx += 1