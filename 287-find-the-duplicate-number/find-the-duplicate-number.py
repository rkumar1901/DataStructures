class Solution(object):
    def findDuplicate(self, nums):

        # Treat nums like a linked list
        slow = nums[0]
        fast = nums[0]

        # Find meeting point inside cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find beginning of cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        