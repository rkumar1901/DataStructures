class Solution(object):
    def removeDuplicateLetters(self, s):

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        stack = []
        seen = set()

        for c in s:

            count[c] -= 1

            if c in seen:
                continue

            while stack and stack[-1] > c and count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(c)
            seen.add(c)

        return ''.join(stack)


        