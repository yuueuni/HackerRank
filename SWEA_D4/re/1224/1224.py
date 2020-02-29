import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D4\\re\\1224\\input.txt')


def postfix(data):
    stack = []
    result = []
    check = False
    i = 0
    while i != len(data):
        d = data[i]
        if d.isdigit():
            result.append(d)
        elif d =='(':
            while d != ')':
                if d.isdigit():
                    result.append(d)
                elif d == '*' or d == '+':
                    stack.append(d)
                i += 1
                d = data[i]
        else:
            stack.append(d)
        i += 1
    return result


for tc in range(1, 2):
    n = int(input())
    data = input()
    result = postfix(data)
    print(f'#{tc} {eval(data)} {result}')
