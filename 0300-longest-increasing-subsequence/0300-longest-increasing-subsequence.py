class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * (n)

        for no in range(n):
            for subsequence in range(no):
                if nums[no] > nums[subsequence]:
                    dp[no] = max(dp[no], dp[subsequence] + 1)
        
        return max(dp)
        