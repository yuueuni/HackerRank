def palindrome(word_length, matrix):
    cnt = 0
    # 가로
    for i in range(8):
        # 세로
        for j in range(8):
            # 회문길이 기준 가로
            for m in range(i, 8):
                # 회문길이 기준 세로
                for n in range(j, 8):
                    # matrix index 범위 벗어나면 넘김
                    if m + word_length > 8 or n + word_length > 8:
                        pass
                    # n고정 m가변 : 가로확인
                    temp += matrix[n][m]
                    # n가변 m 고정 : 세로확인
                    temp += matrix[m][n]

    return cnt


for t in range(10):
    word_length = int(input())
    matrix = [[] * a for a in range(8)]
    for b in range(8):
        matrix[b] = list(input())
    result = palindrome(word_length, matrix)
    print('#{}'.format(t + 1), result)