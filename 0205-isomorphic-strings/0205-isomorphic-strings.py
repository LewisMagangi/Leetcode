class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Convert strings to lists (not necessary but retained as per your original code)
        s = list(s)
        t = list(t)

        # Dictionaries for mapping characters
        st_dict = {}
        ts_dict = {}

        # Check if lengths are the same
        if len(s) != len(t):
            return False
        
        # Zip characters from both strings
        zipped_list = zip(s, t)
        for key, value in zipped_list:
            # Check and update the s-to-t mapping
            if key in st_dict:
                if st_dict[key] != value:
                    return False
            else:
                st_dict[key] = value
            
            # Check and update the t-to-s mapping
            if value in ts_dict:
                if ts_dict[value] != key:
                    return False
            else:
                ts_dict[value] = key
        
        # If all mappings are consistent
        return True