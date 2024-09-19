class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(h) - 1
        result = 0
        while l < r:
            a = min(h[l], h[r]) * (r - l)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
            if a > result:
                result = a
        return result
            

