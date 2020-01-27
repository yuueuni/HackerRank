l = int(input())
for t in range(1, l+1):
    number_list = list(input().split(' '))
    average_number = round(sum(int(x) for x in number_list)/len(number_list))
    print('#{}'.format(t), average_number)