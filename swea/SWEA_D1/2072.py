l = int(input())
for t in range(1, l+1):
    number_list = list(input().split(' '))
    odd_number = sum(int(x) for x in number_list if int(x)%2)
    print('#{}'.format(t), odd_number)