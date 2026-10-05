class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        dic = {}

        for i, ch in enumerate(s):
            dic[ch] = i


        end, size = 0, 0
        res = []

        for i, ch in enumerate(s):
            size += 1
            end = max(end, dic[ch])

            if end == i:
                res.append(size)
                size = 0

        return res
        