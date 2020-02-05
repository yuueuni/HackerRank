import sys

sys.stdin = open('.\input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    d = n//10
    result = 0

    print(f'#{tc} {result}')