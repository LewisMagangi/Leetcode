class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digits_list = [int(digit) for digit in str(x)]
        if digits_list == digits_list[::-1]:
            return True
        return False