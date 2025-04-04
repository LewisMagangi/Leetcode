class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(is_left):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (is_left and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left

        start = binary_search(True)
        end = binary_search(False) - 1

        # Check if target actually exists in nums
        if start <= end and end < len(nums) and nums[start] == target and nums[end] == target:
            return [start, end]
        return [-1, -1]
        