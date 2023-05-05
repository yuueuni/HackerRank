l = int(input())
for t in range(1,l+1):
    number = input().split(' ')
    if number[0] == number[1]:
        print('#{}'.format(t), '=')
    elif number[0] > number[1]:
        print('#{}'.format(t), '>')
    else:
        print('#{}'.format(t), '<')