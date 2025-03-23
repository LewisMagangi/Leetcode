class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)
            for permutation in permutations:
                permutation.append(n)
            result.extend(permutations)
            nums.append(n)
        return result
        