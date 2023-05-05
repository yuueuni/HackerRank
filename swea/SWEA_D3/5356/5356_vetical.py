import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sent = [[] for _ in range(5)]
    for i in range(5):
        sent[i] = list(input())
    res = [len(x) for x in sent]
    result = []
    for _ in range(max(res)):
        for s in sent:
            if not s:
                pass
            else:
                temp = s.pop(0)
                result.append(temp)
    print(f'#{tc}', ''.join(result))