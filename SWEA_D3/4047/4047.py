import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    temp = input()
    cards = list(temp[x:x+3] for x in range(0, len(temp), 3))
    s = d = h = c = 0
    if len(cards) != len(set(cards)):
        print(f'#{tc} ERROR')
    else:
        for card in cards:                
            if card[0] == 'S':
                s += 1
            elif card[0] == 'D':
                d += 1
            elif card[0] == 'H':
                h += 1
            else:
                c += 1
        print(f'#{tc}', 13-s, 13-d, 13-h, 13-c)