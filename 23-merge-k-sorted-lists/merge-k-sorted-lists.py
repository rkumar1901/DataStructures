# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        min_heap = []

        # Put the first node from every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:

            # Get smallest node
            value, i, node = heapq.heappop(min_heap)

            # Add it to result
            curr.next = node
            curr = curr.next

            # Add next node from the same list
            if node.next:
                heapq.heappush(min_heap,(node.next.val, i, node.next))

        return dummy.next

        