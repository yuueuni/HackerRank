import time
from typing import List

"""
1: 육지, 0: 바다
- 섬의 개수 구하기
"""


class Solution:
    grid: List[List[int]]

    def dfs(self, i: int, j: int):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != 1:
            return

        self.grid[i][j] = 0
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)

    def num_islands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 1:
                    self.dfs(i, j)
                    count += 1
        return count


def num_islands(grid: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    return count


if __name__ == '__main__':
    start = time.time()
    matrix = [
        # [1, 1, 1, 1, 0],
        # [1, 1, 0, 1, 0],
        # [1, 1, 0, 0, 0],
        # [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    # solution = Solution()
    # result = solution.num_islands(matrix)
    result = num_islands(matrix)
    end = time.time()
    print(result, end - start)
