
n = int(input())
temp = list(str(x) for x in range(1, n+1))
result = ''
for check in temp:
    cnt = 0
    cnt += check.count('3')
    cnt += check.count('6')
    cnt += check.count('9')
    if cnt == 0:
        result += str(check)+' '
    else:
        result += '-'*cnt + ' '
print(result)