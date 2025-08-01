from collections import Counter

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        freq, count = Counter(nums), 0

        for num in nums:
            if num + diff in freq and num +  (2 * diff) in freq:
                count += 1
        return count