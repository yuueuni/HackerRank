import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\re\\1224\\input.txt')


def postfix(data):
    result = []
    check = False
    bracket = False
    i = temp = tem2 = 0
    while i != len(data):
        d = data[i]
        if d.isdigit():
            if check:
                result.append(d)
                result.append(temp)
                check = False
            else:
                result.append(d)
        elif d =='(':
            while d != ')':
                if d.isdigit():
                    if bracket:
                        result.append(d)
                        result.append(tem2)
                        bracket = False
                    else:
                        result.append(d)
                elif d == '*' or d == '+':
                    tem2 = d
                    bracket = True
                i += 1
                d = data[i]
            result.append(temp)
        else:
            temp = d
            check = True
        i += 1
    return result


for tc in range(1, 2):
    n = int(input())
    data = input()
    result = postfix(data)
    print(f'#{tc} {eval(data)} {result}')
