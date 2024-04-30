from collections import deque

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
    graph = [[-1]*102 for _ in range(102)]
    visited = [[0]*102 for _ in range(102)]
    for rec in rectangle:
        leftX, leftY, rightX, rightY = map(lambda x: x*2, rec)
        for i in range(leftX, rightX+1):
            for j in range(leftY, rightY+1):
                if leftX < i < rightX and leftY < j < rightY:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    dq = deque()
    dq.append((characterX*2, characterY*2))
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    while dq:
        x, y = dq.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] // 2
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0 < nx < 102 and 0 < ny < 102 and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append((nx, ny))
    return answer


if __name__ == '__main__':
    for d in data:
        rectangle = d[0]
        characterX, characterY, itemX, itemY, result = d[1].split(' ')
        res = solution(rectangle, int(characterX), int(characterY), int(itemX), int(itemY))
        print("########", result, res)