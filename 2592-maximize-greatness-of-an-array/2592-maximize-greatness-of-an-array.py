class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        nums.sort()

        for num in nums:
            if num > nums[ans]:
                ans += 1
        
        return ans