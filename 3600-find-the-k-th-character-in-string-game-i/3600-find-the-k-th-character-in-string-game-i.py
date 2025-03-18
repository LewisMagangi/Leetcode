class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        shift = 0
        n = 0

        while(1 << n) < k:
            n += 1

        while n > 0:
            if k > 1 << (n - 1):
                k -= 1 << (n - 1)
                shift += 1
            n -= 1
        return chr(ord('a') + shift)

        