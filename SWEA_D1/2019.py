number = int(input())
temp = 1
for i in range(0, number+1):
    if i == 0:
        print(temp, end=' ')
    else:
        temp *= 2
        print(temp, end=' ')