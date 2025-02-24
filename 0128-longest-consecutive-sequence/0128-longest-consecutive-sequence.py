class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if (i - 1) not in num_set:
                current_no = i
                length = 1

                while (current_no + 1) in num_set:
                    current_no += 1
                    length += 1

                longest = max(longest, length)
        return longest



        