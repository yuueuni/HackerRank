

tc = int(input())
for t in range(tc):
    h1, m1, h2, m2 = map(int, input().split())
    result_hh = h1 + h2
    result_mm = m1 + m2
    if result_mm >= 60:
        result_hh += 1
        result_mm -= 60
    if result_hh > 12:
        result_hh -= 12
    print('#{}'.format(t+1), result_hh, result_mm)