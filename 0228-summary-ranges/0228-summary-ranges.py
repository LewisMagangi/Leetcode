class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if nums[i] == start:
                res.append(str(nums[i]))
            else:
                res.append(str(start) + '->' + str(nums[i]))
            
            i += 1
        return res