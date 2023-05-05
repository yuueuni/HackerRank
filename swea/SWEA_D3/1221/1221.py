import sys

sys.stdin = open('input.txt')

T = int(input())

num = {
    'ZRO':0,
    'ONE':1,
    'TWO':2,
    'THR':3,
    'FOR':4,
    'FIV':5,
    'SIX':6,
    'SVN':7,
    'EGT':8,
    'NIN':9,
}

for _ in range(1, T+1):
    tc, n = input().split()
    data = list(input().split())
    tns = []
    for d in data:
        tns.append(num[d])
    tns.sort()
    result = []
    for t in tns:
        for key, value in num.items():
            if t == value:
                result.append(key)
    print(f'{tc}', *result)