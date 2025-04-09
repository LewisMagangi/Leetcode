class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges, range = [], []

        for num in nums:

            if num - 1 not in range:
                range = []
                ranges += range, # ranges.append(range)
            range[1:] = num,

        return ['->'.join(map(str, range)) for range in ranges]