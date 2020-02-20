import sys

sys.stdin = open('c:\\tensor\\algorithm\\SWEA_D2\\4874\\input.txt')

T = int(input())

def test(datai):
    num = []
    answer = 0
    try:
        while datai:
            current = datai.pop(0)
            if current == '.':
                if len(num) != 1:
                    return 'error'
                return int(float(num[0]))
            elif current.isdigit():
                num.append(current)
            else:
                temp = num.pop(-2) + current + num.pop(-1)
                num.append(str(eval(temp)))
    except:
        return 'error'



for tc in range(1, T+1):
    data = list(input().split())
    result = test(data)
    print(f'#{tc} {result}')