class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = [int(i) for i in str(n)]
        product.sort()

        return int(product[-1]) * int(product[-2])