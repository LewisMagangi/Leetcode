class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        # List comprehension to keep only unique elements and maintain order
        nums[:] = [x for x in nums if x not in seen and not seen.add(x)]
        # Return the length of the modified list
        return len(nums)