class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1]
        for i in nums:
            rob1, rob2 = rob2, max(i + rob1, rob2)
        return rob2


        