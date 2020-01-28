tc = int(input())

for i in range(tc):
    num1, num2 = input().split(' ')
    quotient, remainder = divmod(int(num1), int(num2))
    print('#{}'.format(i+1), quotient, remainder)
