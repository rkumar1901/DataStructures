class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Determine smaller and larger array to minimize binary search range
        smaller = nums2 if len(nums1) > len(nums2) else nums1
        larger = nums1 if len(nums1) > len(nums2) else nums2
        
        totalLength = len(nums1) + len(nums2)
        
        low = 0
        high = len(smaller)
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (totalLength + 1) // 2 - partitionX
            
            # Left and right boundary values for smaller array
            l1 = float('-inf') if partitionX == 0 else smaller[partitionX - 1]
            r1 = float('inf') if partitionX == len(smaller) else smaller[partitionX]
            
            # Left and right boundary values for larger array
            l2 = float('-inf') if partitionY == 0 else larger[partitionY - 1]
            r2 = float('inf') if partitionY == len(larger) else larger[partitionY]
            
            # Check if partition is valid
            if l1 <= r2 and l2 <= r1:
                if totalLength % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return float(max(l1, l2))
            
            # Adjust binary search range
            if l1 > r2:
                high = partitionX - 1
            else:
                low = partitionX + 1
                
        return 0.0
        