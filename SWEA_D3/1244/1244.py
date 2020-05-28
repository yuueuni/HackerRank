import sys

sys.stdin = open('input.txt')

# def find(card, count):
#     temp = int(''.join(card))
#     if maxnum <= temp:
#         maxnum = temp
#     if count == cnt:
#         return
#     else:
#         for i in range(len(card)):
#             for j in range(1, len(card)):
#                 card[i], card[j] = card[j], card[i]
#                 find(card, count+1)
#                 card[i], card[j] = card[j], card[i]

# tc = int(input())
# for t in range(1, tc+1):
#     n, cnt = input().split()
#     card = list(n)
#     maxnum = int(''.join(card))
#     find(card, 0)
#     print(f'#{t} {card}')




def find(n, k, c):
    global maxV
    global minC
    if c == 0 or n == k:
        s = int(''.join(card))
        if (maxV <= s):
            maxV = s
            if (minC > c):
                minC = c
    else:
        for i in range(k):
            card[n], card[i] = card[i], card[n]
            cnt = 1 if n != i else 0
            find(n+1, k, c-cnt)
            card[n], card[i] = card[i], card[n]

t = int(input())
for tc in range(1, t+1):
    c, N = input().split()
    card = list(c)
    maxV = int(''.join(card))
    minC = int(N)
    find(0, len(card), int(N))
    if minC % 2 != 0:
        temp = list(str(maxV))
       	temp[-2], temp[-1] = temp[-1], temp[-2]
        maxV = ''.join(temp)
    print(f'#{tc} {maxV}')