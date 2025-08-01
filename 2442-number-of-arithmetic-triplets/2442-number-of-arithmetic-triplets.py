class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        seen, count = set(nums), 0

        for num in nums:
            if num + diff in seen and num + 2*diff in seen:
                count += 1
        return count