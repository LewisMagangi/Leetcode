class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        k_distance_indices = []
        j_indices = [index for index, num in enumerate(nums) if nums[index] == key]

        for i in range(len(nums)):
            for j in j_indices:
                if abs(i - j) <= k and nums[j] == key:
                    k_distance_indices += [i]
                    break

        return k_distance_indices