import sys

sys.stdin = open('input.txt')


def test(n, m, ar, am):
    temp = n - m
    arr = []
    if temp < 0:
        for i in range(abs(temp)+1):
            res = 0
            listA = [0]*i + ar + [0]*(abs(temp)-i)
            for x, y in zip(listA, am):
                res += x*y
            arr.append(res)
    else:
        for i in range(abs(temp)+1):
            res = 0
            listB = [0]*i + am+ [0]*(abs(temp)-i)
            for x, y in zip(listB, ar):
                res += x*y
            arr.append(res)
    return max(arr)


tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    num_n = list(map(int, input().split()))
    num_m = list(map(int, input().split()))
    result = test(N, M, num_n, num_m)
    print('#{}'.format(t+1), result)