import sys

sys.stdin = open('input.txt')

def test(data):
    result = []
    temp = []
    while data:
        d = data.pop(0)
        if d == '(':
            d = data.pop(0)
            while True:
                if d.isdigit():
                   result.append(d)
                elif d == ')':
                    break
                else:
                    temp.append(d)
        if d.isdigit():
            result.append(d)
        else:
            temp.append(d)

    return 1


for tc in range(1, 11):
    n = int(input())
    data = input()
    result = test(data)
    print(f'#{tc} {eval(data)} {result}')
