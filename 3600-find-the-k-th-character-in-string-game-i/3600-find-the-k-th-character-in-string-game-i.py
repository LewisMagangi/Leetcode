class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        def generate(n):
            if n == 0:
                return "a"
            
            prev = generate(n - 1)
            transformed = ''.join(chr(ord(i) + 1) for i in prev)
            return prev + transformed

        n = 0
        while len(generate(n)) < k:
            n += 1
        
        return generate(n)[k - 1]


        