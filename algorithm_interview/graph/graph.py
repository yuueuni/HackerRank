import time
from typing import List


class Graph:
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3],
    }

    def dfs(self, v: int, discovered: List[int] = []) -> List[int]:
        # 깊이 우선 탐색
        discovered.append(v)
        for w in self.graph[v]:
            if w not in discovered:
                discovered = self.dfs(w, discovered)
        return discovered

    def bfs(self, v: int) -> List[int]:
        # 너비 우선 탐색
        discovered = []
        stack = [v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in self.graph[v]:
                    stack.append(w)
        return discovered


if __name__ == '__main__':
    start = time.time()
    result = Graph().bfs(1)
    end = time.time()
    print(result, end - start)