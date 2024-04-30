# maps answer
from collections import deque

inputs = [
    [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]], 11],
    [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]], -1]
]


def solution(maps):
    n, m = len(maps), len(maps[0])

    visited = [[False] * m for _ in range(n)]

    dq = deque()
    dq.append((0, 0, 1))
    visited[0][0] = True

    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    while dq:
        x, y, cnt = dq.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt + 1))
    return -1


def solution_2(maps):
    n, m = len(maps), len(maps[0])

    visited = [[False] * m for _ in range(n)]

    dq = deque()
    dq.append((0, 0, 1))
    visited[0][0] = True

    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    while dq:
        x, y, cnt = dq.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt + 1))
    return -1


if __name__ == "__main__":
    for inp in inputs:
        maps, answer = inp[0], inp[1]
        res = solution(maps)
        print(res, answer)
