import collections
import time

"""
이진트리 직렬화, 역직렬화
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        if data == '# #':
            return None
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


if __name__ == '__main__':
    start = time.time()
    nodes = TreeNode([3, 9, 20, None, None, 15, 7])
    result = Solution().serialize(nodes)
    # result = Solution().deserialize('# 1 2 3 # # 4 5 # # # #')
    end = time.time()
    print(result, end - start)
    # print(result2, end - start)
