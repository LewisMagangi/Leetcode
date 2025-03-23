class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for num in nums:
            new_result = []
            for permutation in result:
                for i in range(len(permutation) + 1):
                    new_result.append(permutation[:i] + [num] + permutation[i:])
            result = new_result
        return result
