import sys

sys.stdin = open('input.txt')

n = int(input())
data = {}
for _ in range(n):
    l, h = map(int, input().split())
    data[l] = h

print(data)