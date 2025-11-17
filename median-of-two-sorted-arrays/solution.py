class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        merged_array = nums1 + nums2
        
        sorted_array = sorted(merged_array)

        n = len(sorted_array)
        
        if n == 0:
            return 0.0

        if n % 2 == 1:
            median = float(sorted_array[n // 2])
        else:
            mid1 = sorted_array[(n // 2) - 1]
            mid2 = sorted_array[n // 2]
            median = (mid1 + mid2) / 2.0

        return median
