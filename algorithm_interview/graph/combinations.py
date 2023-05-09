import itertools
import time
from typing import List

"""
n까지 수 중 k개 조합
"""


class Solution:

    def solution(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


if __name__ == '__main__':
    start = time.time()
    n, k = 4, 2
    result = Solution().solution(n, k)
    end = time.time()
    result2 = list(map(list, itertools.combinations(range(1, n + 1), k)))
    print(result2)
    print(result, end - start)
