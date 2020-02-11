# import sys

# sys.stdin = open('input.txt')

n = int(input())

max_cnt = second = 0
while second <= n:
    temp = []
    temp.append(n)
    temp.append(second)
    nx = n - second
    idx = 2
    while nx >= 0:
        temp.append(nx)
        nx = temp[idx-1]-temp[idx]
        idx += 1
    if len(temp) > max_cnt:
        max_cnt = len(temp)
        result = temp
    second += 1
print(max_cnt)
print(*result)