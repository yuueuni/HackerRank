# n computers return
inputs = [
    [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
    [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1]
]


def solution(n, computers):
    def DFS(i):
        visited[i] = True
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)

    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    return max(answer, 1)



if __name__ == "__main__":
    for inp in inputs:
        n, computers, result = inp[0], inp[1], inp[2]
        res = solution(n, computers)
        print(res, result)