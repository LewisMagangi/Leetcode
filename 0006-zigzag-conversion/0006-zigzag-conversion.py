class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s

        current_row = 0
        rows = ['']*numRows
        going_down = True

        for i in range(len(s)):
            rows[current_row] += s[i] 
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        return ''.join(rows)
            
        