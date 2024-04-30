# n computers return
from collections import deque

inputs = [
    [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
    [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1]
]


def solution(n, computers):

    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            idx = q.popleft()
            visited[idx] = True
            for j in range(n):
                if computers[idx][j] and not visited[j]:
                    q.append(j)

    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer


if __name__ == "__main__":
    for inp in inputs:
        n, computers, result = inp[0], inp[1], inp[2]
        res = solution(n, computers)
        print(res, result)