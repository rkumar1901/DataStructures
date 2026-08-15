from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = Counter(s)

        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = ""

        prev_count = 0
        prev_char = None

        while heap:

            count, char = heapq.heappop(heap)

            # Put previous character back into heap because it is now safe to use again
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            result += char
            count += 1

            # Hold this character out of the heap
            prev_count = count
            prev_char = char

        # If something is left over, impossible
        if prev_count < 0:
            return ""

        return result
        