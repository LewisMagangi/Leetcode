class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for num in nums:
            
            if not ranges or num > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = num,
            
        return ['->'.join(map(str, i)) for i in ranges]

            
        