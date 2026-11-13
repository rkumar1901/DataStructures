class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, x, y))

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
        