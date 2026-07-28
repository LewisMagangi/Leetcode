class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0

        l = len(nums)

        marked = [False] * l

        pairs = [(nums[i], i) for i in range(l)]

        pairs.sort()

        for value, index in pairs:
            if not marked[index]:
                marked[index] = True
                score += value

                if index > 0:
                    marked[index - 1]  = True
                
                if index < len(pairs) - 1:
                    marked[index + 1] = True
        
        return score