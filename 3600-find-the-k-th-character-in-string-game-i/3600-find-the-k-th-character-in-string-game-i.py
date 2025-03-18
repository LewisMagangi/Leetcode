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
            half = 1 << (n - 1)
            if k > half:
                k -= half
                shift += 1
            n -= 1
        return chr(ord('a') + shift)

        