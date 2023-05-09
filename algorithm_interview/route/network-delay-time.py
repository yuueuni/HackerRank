import collections
import heapq
import time


class Solution:

    def solution(self, times, n, k):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == n:
            return max(dist.values())
        return -1


if __name__ == '__main__':
    start = time.time()
    nodes = [
        [2, 1, 1],
        [2, 3, 1],
        [3, 4, 1],
    ]
    n, k = 4, 2
    result = Solution().solution(nodes, n, k)
    end = time.time()
    print(result, end - start)
