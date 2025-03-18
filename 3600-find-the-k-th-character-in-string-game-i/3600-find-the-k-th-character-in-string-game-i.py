class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        def length(n):
            return 1 << n
        
        def find(n, k):
            if n == 0:
                return 'a'

            prev_len = length(n - 1)

            if prev_len >= k:
                return find(n - 1, k)
            else:
                original_char = find(n - 1, k - prev_len)
                return chr(ord(original_char) + 1)

        n = 0
        while length(n) < k:
            n += 1
        
        return find(n, k)

            


        