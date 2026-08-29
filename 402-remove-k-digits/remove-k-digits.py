class Solution(object):
    def removeKdigits(self, num, k):

        r = 0
        stack = []

        for r in num:

            while stack and k > 0 and stack[-1] > r:
                stack.pop()
                k -= 1

            stack.append(r)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')

        return result if result else '0'      