import sys

sys.stdin = open('input.txt')

T = int(input())

def find(datai, ni):
    idx = []
    for i in range(ni):
        for j in range(ni):
            cnt_i = cnt_j = 1
            if datai[i][j]:
                t = 0
                while 1:
                    if datai[i+t][j]:
                        cnt_i = t + 1
                        for k in range(ni-j):
                            if datai[i+t][j+k]:
                                cnt_j = k + 1
                                datai[i+t][j+k] = 0
                            else:
                                break
                        t += 1
                    else:
                        break
                idx.append([cnt_i, cnt_j])
    return idx


for tc in range(1, T+1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split()))+[0])
    result = find(data, n)
    
    s_result = []
    for r in result:
        temp = r[0]*r[1]
        s_result.append([temp, r[0], r[1]])
    s_result.sort()
    
    # 출력
    print(f'#{tc}', len(result), end =' ')
    for sr in s_result:
        stemp = sr[1:]
        print(*stemp, end=' ')
    print()