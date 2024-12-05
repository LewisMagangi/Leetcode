class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ir = {
            'M' : 1000,
            'CM' : 900,
            'D' : 500,
            'CD' : 400,
            'C' : 100,
            'XC': 90,
            'L' : 50,
            'XL' : 40,
            'X' : 10,
            'IX' : 9,
            'V' : 5,
            'IV' : 4,
            'I' : 1,
        }

        rom = ''
        i = 0
        l = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V','IV', 'I']
        
        for i in range(len(l)):
            while num >= ir[l[i]]:
                num -= ir[l[i]] #find the value not the key
                rom += l[i]
        
        return rom