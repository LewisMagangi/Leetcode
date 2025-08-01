class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        
        i, j, k = 0, 1, 2
        count = 0
        n = len(nums)

        while i < n - 2:            
            while j < n - 1 and nums[j] - nums[i] < diff:
                j += 1

            while k < n and nums[k] - nums[j] < diff:
                k += 1
            
            if j < n and k < n and nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                count += 1

            i += 1
            j = max(j, i + 1)
            k = max(k, j + 1)
        
        return count