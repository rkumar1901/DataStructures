class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return 1

        a, b = 1, 1  # a = f(0), b = f(1)

        for _ in range(2, n + 1):
            a, b = b, a + b  # Update to f(n-1), f(n)

        return b
        