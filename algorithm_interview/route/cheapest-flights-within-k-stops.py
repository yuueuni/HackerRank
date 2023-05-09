import collections
import heapq
import time


class Solution:

    def solution(self, n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        Q = [(0, src, k)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1


if __name__ == '__main__':
    start = time.time()
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src, dst, n, k = 0, 2, 3, 0
    result = Solution().solution(n, edges, src, dst, k)
    end = time.time()
    print(result, end - start)
