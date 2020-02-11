import sys

sys.stdin = open('input.txt')

swi = int(input())

def onoff(a):
    if a == 1:
        return 0
    else:
        return 1

def change(datai, gen, ni, swii):
    if gen==1:
        i = 1
        x = ni
        while x-1 < swii:
            datai[x-1] = onoff(datai[x-1])
            i += 1
            x = ni*i
    else:
        idx = 1
        while (ni+idx+1) <swii and (ni-idx-1)>=0:
            temp = datai[ni-idx-1:ni+idx]
            if temp == temp[::-1]:
                ans = idx
            idx += 1
        for d in range(ni-ans-1, ni+ans):
            datai[d] = onoff(datai[d])
    return datai


data = list(map(int, input().split()))
stn = int(input())
for _ in range(stn):
    gender, number = map(int, input().split())
    data = change(data, gender, number, swi)

for da in range(len(data)):
    print(data[da], end=' ')
    if da % 20 == 0 and da != 0:
        print()