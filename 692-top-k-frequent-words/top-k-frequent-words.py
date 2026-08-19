class Solution(object):
    def topKFrequent(self, words, k):

        dic = {}

        for i in words:
            dic[i] = 1 + dic.get(i, 0)

        sor = sorted(dic, key=lambda x: (-dic[x], x))

        return sor[:k]


        