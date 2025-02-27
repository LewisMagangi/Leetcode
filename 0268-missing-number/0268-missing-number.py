class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Methods to solve this

        1. Sort and iterate through once to find the missing no in nums. Complexity Time - O(n log n) due to sorting,
        Memory O(n) due to the space used to store the sorted list if we'll create a separate list 
        but if we sort in place Memory O(1)

        2. Using a hashset for fast lookups. Comp Time - O(1), Mem - O(n) due to space for set.

        3. Floyd's Algorithm (Slow and fast pointers) Linked lists. Complexity Time O(n), Mem O(1)
        """
        nums = set(nums) 

        for i in range(0, len(nums)):
            if i not in nums:
                return i
        return len(nums)
