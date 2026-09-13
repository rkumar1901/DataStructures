from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        result = 0

        for i in range(len(points)):

            slopes = defaultdict(int)

            x1, y1 = points[i]

            for j in range(i + 1, len(points)):

                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                # Make the direction consistent
                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1

                slopes[(dy, dx)] += 1

                result = max(result, slopes[(dy, dx)] + 1)

        return result
        