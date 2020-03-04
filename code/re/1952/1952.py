import sys

sys.stdin = open('c:\\yooncode\\algorithm\\code\\re\\1952\\input.txt')

T = int(input())

def test(plan, pay, y, i):
    if i >= 12:
        return pay
    elif min(pay.values())>=y:
        return y

for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    pay = {d:0, m:0, m3:0}
    plan = list(map(int, input().split()))
    result = test(plan, pay, y, 0)
    print(f'#{tc} {result}')