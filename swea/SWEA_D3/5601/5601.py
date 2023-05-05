import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = [('1/'+str(n)) for _ in range(n)]
    print(f'#{tc}', *result)