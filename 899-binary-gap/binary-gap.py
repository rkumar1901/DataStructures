class Solution:
    def binaryGap(self, n: int) -> int:

        x = bin(n)[2:]

        count_zero = 0
        append = False
        max_res = 0

        for r in x:

            if r == "1":
                if append:
                    max_res = max(count_zero + 1, max_res)

                append = True
                count_zero = 0

            else:
                count_zero += 1

        return max_res

        