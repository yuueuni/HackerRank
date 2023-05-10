import collections
import time

"""
이진 트리 최대 깊이
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def solution(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth


if __name__ == '__main__':
    start = time.time()
    nodes = TreeNode([3, 9, 20, None, None, 15, 7])
    result = Solution().solution(nodes)
    end = time.time()
    print(result, end - start)
