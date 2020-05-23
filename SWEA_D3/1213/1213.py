import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    search = input()
    strs = input()
    t = strs.count(search)
    print(f'#{tc} {t}')