import sys


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    test = input()
    s = []
    balance = True
    idx = 0
    print()