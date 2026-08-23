import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """

        courses.sort(key=lambda x: x[1])

        max_heap = []
        total_time = 0

        for duration, deadline in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            # We exceeded the deadline
            if total_time > deadline:
                longest_course = -heapq.heappop(max_heap)
                total_time -= longest_course

        return len(max_heap)
        