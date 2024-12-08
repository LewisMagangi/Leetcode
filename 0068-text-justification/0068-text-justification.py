class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []   
        current_line, char_line_length = [], 0 

        for word in words:
            if char_line_length + len(word) + len(current_line) > maxWidth: # The len(current_line) handles a single space min
                extra_spaces = maxWidth - char_line_length

                for i in range (extra_spaces):
                    current_line[i % (len(current_line) - 1 or 1 )] += ' '
                res.append(''.join(current_line))
                current_line, char_line_length = [], 0
            
            current_line.append(word)
            char_line_length += len(word)
        
        res.append(' '.join(current_line).ljust(maxWidth))

        return res
        
        