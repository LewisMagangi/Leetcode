class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        guess = x

        while guess * guess > x:
            guess = (guess + x // guess) // 2
        
        return guess