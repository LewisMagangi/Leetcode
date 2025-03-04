class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sl = nums1 + nums2
        sl.sort()
        l_len = len(sl)
        middle_index = l_len // 2

        if l_len % 2 == 0:
            return (sl[middle_index] + sl[middle_index - 1]) / 2.0
        else:
            return sl[middle_index]