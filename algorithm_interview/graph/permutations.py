import itertools
import time
from typing import List
"""
순열
"""


class Solution:

    def solution(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


if __name__ == '__main__':
    start = time.time()
    inputs = [1, 2, 3]
    result = Solution().solution(inputs)
    iter_result = list(map(list, itertools.permutations(inputs)))
    print('itertools', iter_result)
    end = time.time()
    print(result, end - start)