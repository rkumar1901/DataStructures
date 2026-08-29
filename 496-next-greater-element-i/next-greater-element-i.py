class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        dic = {}
        res = []

        for r in nums2:

            while stack and stack[-1] < r:
                num = stack.pop()
                dic[num] = r

            stack.append(r)

        for i in nums1:
            if i in dic:
                res.append(dic[i])
            else:
                res.append(-1)

        return res

                




        