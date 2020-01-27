# 가위는 1, 바위는 2, 보는 3
personA, personB = map(int, input().split(' '))

if personA-personB >0:
    if personA == 3 and personB == 1:
        result = 'B'
    else:
        result = 'A'
elif personA == 1 and personB == 3:
    result = 'A'
else:
    result = 'B'
    
print(result)