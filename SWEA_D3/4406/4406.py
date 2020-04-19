import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input())
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [d for d in data if d not in vowels]
    print(f'#{tc}', ''.join(result))