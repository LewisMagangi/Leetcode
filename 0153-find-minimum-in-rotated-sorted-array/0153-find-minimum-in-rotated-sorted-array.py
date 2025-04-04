class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Minimum is at mid or in the left half
                right = mid

        return nums[left]
        