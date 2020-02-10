import sys

sys.stdin = open('c:\\Users\\jin89\\Desktop\\algorithm\\SWEA_D3\\1216\\input.txt')

def find(datai):
    result = 0
    for i in range(100):
        for j in range(100):
            for n in range(100-j, 0, -1):
                word = datai[i][j:j+n]
                if word == word[::-1]:
                    if result < n:
                        result = n
    return result


for _ in range(10):
    tc = int(input())
    data = []
    for _ in range(100):
        data.append(list(input()))
    res_a = find(data)
    for _ in range(1):
        data = list(zip(*data[::-1]))
    res_b = find(data)
    if res_a < res_b:
        answer = res_b
    else:
        answer = res_a
    print(f'#{tc} {answer}')