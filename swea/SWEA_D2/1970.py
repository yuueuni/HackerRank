tc = int(input())
for t in range(tc):
    n = int(input())
    money = { 50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0 }
    print('#{}'.format(t+1))
    for key in money:
        temp = n // key
        money[key] = temp
        n -= temp * key
    print(' '.join(map(str, money.values())))