def snailNumber(n):
    direction_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num = 0
    direction_index = 0
    current_r, current_c = 0, -1
    array = [[-1] * n for i in range(n)]

    while num < n * n:
        dir = direction_list[direction_index]
        temp_r = current_r + dir[0]
        temp_c = current_c + dir[1]

        if temp_c < 0 or temp_r < 0 or temp_c >= n or temp_r >= n or array[temp_r][temp_c] != -1:
            direction_index += 1
            if direction_index == 4:
                direction_index = 0
        else:
            num += 1
            current_r, current_c = temp_r, temp_c
            array[current_r][current_c] = num

    return array


tc = int(input())
for t in range(tc):
    test = int(input())
    result = snailNumber(test)
    print('#{}'.format(t+1))
    for r in result:
        print(' '.join(map(str, r)))