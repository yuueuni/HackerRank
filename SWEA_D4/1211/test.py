import sys


sys.stdin = open('input.txt')

def find_path(A, x, y, num):
    while y>0:
        if A[y][x-1]:
            while A[y][x-1]:
                x -= 1
                num += 1
            y -= 1
            num += 1
        elif A[y][x+1]:
            while A[y][x+1]:
                x += 1
                num += 1
            y -= 1
            num += 1
        else:
            y -= 1
            num += 1
    return x, num
 
for index_num in range(10):
    N=int(input())
    A=[]
    for y in range(100):
        A.append([0]+[int(x)for x in input().split()]+[0])
    index = [m if i==1 else -1 for m, i in enumerate(A[99])]
    index = list(filter(lambda a: a != -1, index))
 
    s, x_index = [], []
    for i in index:
        x, y = i, 99
        s.append(find_path(A, x, y, 0)[1])
        x_index.append(find_path(A, x, y, 0)[0])
    n = list(reversed(s)).index(min(s))
    ans = x_index[len(s) - n -1]-1
    print("#%d %d"%(index_num+1,ans))