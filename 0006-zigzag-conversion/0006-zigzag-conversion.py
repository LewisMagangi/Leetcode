class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s

        cr = 0
        rows = ['']*numRows
        gd = True

        for i in range(len(s)):
            rows[cr] += s[i] 
            if cr == 0:
                gd = True
            elif cr == numRows - 1:
                gd = False
            
            if gd:
                cr += 1
            else:
                cr -= 1
        
        return ''.join(rows)
            
        