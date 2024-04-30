from heapq import heappush, heappop

# rectangle characterX characterY itemX itemY result
data = [
[[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],'1 3 7 8 17'],
[[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],'9 7 6 1 11'],
[[[1,1,5,7]],'1 1 4 7 9'],
[[[2,1,7,5],[6,4,10,10]],'3 1 7 10 15'],
[[[2,2,5,5],[1,3,6,4],[3,1,4,6]],'1 4 6 3 10'],
]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 직사각형 테두리 중 가장 바깥 테두리 찾기
    # 테두리: 1, 안쪽: 0, 바깥쪽: -1
    # 1칸 테두리 확인 위해 2배로 늘림
    path = [[-1]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    for rec in rectangle:
        left_x, left_y, right_x, right_y = map(lambda x:x*2, rec)
        for i in range(left_x, right_x + 1):
            for j in range(left_y, right_y + 1):
                if left_x < i < right_x and left_y < j < right_y:
                    path[i][j] = 0
                if path[i][j] != 0:
                    path[i][j] = 1
    # 이동경로 확인
    heap = [(0, characterX * 2, characterY * 2)]
    while heap:
        dist, x, y = heappop(heap)
        if x == itemX * 2 and y == itemY * 2:
            answer = dist // 2
            break
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < 102 and 0 < ny < 102 and not visited[nx][ny]:
                if path[nx][ny] == 1:
                    heappush(heap, (dist + 1, nx, ny))
    return answer


if __name__ == '__main__':
    for d in data:
        rectangle = d[0]
        characterX, characterY, itemX, itemY, result = d[1].split(' ')
        res = solution(rectangle, int(characterX), int(characterY), int(itemX), int(itemY))
        print("########", result, res)