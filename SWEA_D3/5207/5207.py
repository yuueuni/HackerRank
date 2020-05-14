import sys

sys.stdin = open('input.txt')

t = int(input())

# dire > 왼: -1, 오:1, 처음: 0
def find(start, end, dire, number, data):
    global result
    middle = (start+end)//2
    if number == data[middle]:
        result += 1
    elif number > data[middle] and dire != 1:
        find(middle+1, end, 1, number, data)
    elif number < data[middle] and dire != -1:
        find(start, middle-1, -1, number, data)
    else:
        return 0
            

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    for i in b:
        find(0, n-1, 0, i, a)
    print(f'#{tc} {result}')


# ---------------------------------------------------------------------
t = int(input())

def find(start, end, dire, number, data):
    while True:
        middle = (start+end)//2
        if number == data[middle]:
            return 1
        elif number > data[middle] and dire != 1:
            start = middle + 1
            dire = 1
        elif number < data[middle] and dire != -1:
            end = middle - 1
            dire = -1
        else:
            return 0

for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    a.sort()
    for i in b:
        result += find(0, n-1, 0, i, a)
    print(f'#{tc} {result}')