import sys

sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t+1):
    scores = list(map(int, input().split()))
    answer = 0
    for s in scores:
        if s < 40:
            answer += 40
        else:
            answer += s
    answer /= len(scores)
    print(f'#{tc} {round(answer)}')