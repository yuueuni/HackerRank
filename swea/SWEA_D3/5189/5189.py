import sys

sys.stdin = open('c:\\yooncode\\algorithm\\SWEA_D3\\5189\\input.txt')


T = int(input())

def find(i, battery):
    global result
    if battery < result:
        v[i] = 1
        # 모든 구역 방문한 경우
        if 0 not in v:
            # 다시 사무실로 (마지막 배터리 소모)
            battery += data[i][0]
            # 최소 배터리 값 비교
            if result > battery:
                result = battery
        # 해당 구역 방문 안한 경우
        else:
            # 갈 수 있는 구역 탐색
            for k in range(1, len(data)):
                # 아직 방문 안한 구역
                if not v[k] and i != k:
                    find(k, battery+data[i][k])
        v[i] = 0
    else:
        pass


for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    v = [0 for _ in range(n)]
    result = 1000
    find(0, 0)
    print(f'#{tc} {result}')