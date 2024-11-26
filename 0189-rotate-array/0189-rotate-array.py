class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)
        k %= r
        def reverse(l, r):
            while l < r:
                nums[l], nums[r - 1] = nums[r - 1], nums[l]
                l += 1
                r -= 1
        
        reverse(l, r)

        reverse(l, k)

        reverse(k, r)


        