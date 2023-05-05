import sys
from itertools import combinations


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 제한된 칼로리 내에서 최고 점수
    n, l = map(int, input().split())
    taste = []
    calorie = []
    for i in range(n):
        # 점수 T, 칼로리 K
        t, k = map(int, input().split())
        taste.append(t)
        calorie.append(k)