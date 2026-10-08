class Solution:
    def findMin(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1


        if nums[l] < nums[r]:
            return nums[l]

        else:

            while l < r:

                mid = (l + r) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1

                else:
                    r = mid
        
            return nums[l] 
        