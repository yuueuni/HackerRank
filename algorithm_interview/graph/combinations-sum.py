import time

"""
조합의 합
"""


class Solution:

    def solution(self, candidates, target):
        results = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                results.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return results


if __name__ == '__main__':
    start = time.time()
    candidates = [2, 3, 6, 7]
    target = 7
    result = Solution().solution(candidates, target)
    end = time.time()
    print(result, end - start)
