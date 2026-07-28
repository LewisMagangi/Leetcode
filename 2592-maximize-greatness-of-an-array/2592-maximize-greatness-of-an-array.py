class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        i = 0
        
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                ans += 1
                i += 1
        
        return ans