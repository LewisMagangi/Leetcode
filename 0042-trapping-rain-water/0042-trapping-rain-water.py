class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        res = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        
        return res
        