import sys
sys.stdin = open('input.txt')

k = int(input())

data = {1:[], 2:[], 3:[], 4:[]}
position = []
idx = [0, 0]
for _ in range(6):
    p, l = input().split()
    data[int(p)].append(int(l))
    position.append(int(p))

cnt_two = list(x for x in range(1, 5) if position.count(x)==2)
cnt_one = list(x for x in range(1, 5) if position.count(x)==1)
teo = position.index(cnt_two[0])
tew = position.index(cnt_two[1])

if teo < tew:
    no_area = data[cnt_two[1]][0]*data[cnt_two[0]][1]
else:
    no_area = data[cnt_two[0]][0]*data[cnt_two[1]][1]

all_area = data[cnt_one[0]][0]*data[cnt_one[1]][0]
print((all_area - no_area)*k)