import sys

sys.stdin = open('input.txt')

n = int(input())
data = []
for _ in range(n):
    a,b,c,d,e,f = map(int, input().split())
    temp = [ [a,f], [b,d], [c,e] ]
    data.append(temp)


for i in range(n):
    cpdata = data
    temp = cpdata[i].pop(i)
    idx = 1
    while idx<6:
        for j in range(3):
            if temp[0] in data[idx][j]
            temp[1] in data[idx][j]:
                temp = cpdata[idx].pop(j)
        idx += 1
    
    for c in cpdata:

