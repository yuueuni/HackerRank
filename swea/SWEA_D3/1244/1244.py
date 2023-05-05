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


# ------------------------------------------------------------
t = int(input())
maxsize = 720 # 6!

def swap(prize, i, j):
    numArr = [0] * numOfcard
    for k in range(numOfcard-1, -1, -1):
        numArr[k] = prize % 10
        prize //= 10
    numArr[i], numArr[j] = numArr[j], numArr[i]
    prize = 0
    for k in range(numOfcard):
        prize = prize * 10 + numArr[k]
    return prize

def findMax(prize, num, k):
    global ans
    # 메모이제이션 및 가지치기
    for i in range(maxsize):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return

    if k == num:
        if prize > ans: ans = prize
    else:
        for i in range(numOfcard-1):
            for j in range(i+1, numOfcard):
                findMax(swap(prize, i, j), num, k+1)

for tc in range(1, t+1):
    prize, num = map(int, input().split())
    memo = [[0] * maxsize for _ in range(num+1)]
    numOfcard = 0
    ans = 0
    t = prize
    while t:
        t //= 10
        numOfcard += 1
    
    findMax(prize, num, 0)
    print(f'#{tc} {ans}')