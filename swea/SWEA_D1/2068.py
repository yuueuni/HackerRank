l = int(input())
for t in range(1,l+1):
    number_list = map(int, input().split(' '))
    max_number = max(number_list)
    print('#{}'.format(t), max_number)