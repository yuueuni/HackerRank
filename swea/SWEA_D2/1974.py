def test(sdoku):
    for s in sdoku:
        if len(set(s)) != 9:
            return 0

    for h in range(9):
        horizon = list(sdoku[x][h] for x in range(9))
        if len(set(horizon)) != 9:
            return 0

    for i in range(3):
        for j in range(3):
            temp = []
            for a in range(3):
                for b in range(3):
                    temp.append(sdoku[3 * i + a][3 * j + b])
            if len(set(temp)) != 9:
                return 0
    return 1


tc = int(input())
for t in range(tc):
    sdoku = [[0] * n for n in range(9)]
    for i in range(9):
        sdoku[i] = list(map(int, input().split()))
    result = test(sdoku)
    print('#{}'.format(t + 1), result)