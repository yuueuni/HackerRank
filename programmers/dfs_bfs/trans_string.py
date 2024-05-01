# begin, target, words, result
from collections import deque

inputs = [
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0]
]


def solution(begin, target, words):
    words = [begin] + words
    visited = [False] * len(words)
    answer = 0

    dq = deque()
    dq.append((0, 0))
    while dq:
        idx, cnt = dq.popleft()
        if words[idx] == target:
            answer = cnt
            break
        for j in range(1, len(words)):
            if visited[j]:
                continue
            diff = sum(1 for a, b in zip(words[idx], words[j]) if a != b)
            if diff == 1:
                visited[j] = True
                dq.append((j, cnt + 1))
    return answer


if __name__ == "__main__":
    for inp in inputs:
        begin, target, words, result = inp[0], inp[1], inp[2], inp[3]
        res = solution(begin, target, words)
        print(res, result)
