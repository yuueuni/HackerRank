import sys

sys.stdin = open('input.txt')

def maxvh(vh):
    max_vh = 0
    vh.sort()
    for i in range(len(vh)-1):
        if max_vh < vh[i+1] - vh[i]:
            max_vh = vh[i+1] - vh[i]
    return max_vh


# 가로, 세로 max>100
w, hi = map(int, input().split())
vc = [0, hi]
hc = [0, w]
cut = int(input())
for _ in range(cut):
    vhn, n = map(int, input().split())
    if vhn: #세로
        hc.append(n)
    else: #가로
        vc.append(n)
max_v = maxvh(vc)
max_h = maxvh(hc)
print(max_v * max_h)