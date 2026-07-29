class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_1 = max_2 = 0

        while n:
            rem = n % 10

            if rem >= max_1:
                max_2 = max_1
                max_1 = rem
            elif rem > max_2:
                max_2 = rem
            
            n //= 10
        
        return max_1 * max_2
