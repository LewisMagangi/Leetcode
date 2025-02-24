class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        # steps st_dict and ts_dict
        st_dict, ts_dict = {}, {}


        # zipping only and iterating thet turple like a dict and checking st and then ts
        for key, value in zip(s, t):
            if key in st_dict:
                if st_dict[key] != value:
                    return False
            else:
                st_dict[key] = value
            

            if value in ts_dict:
                if ts_dict[value] != key:
                    return False
            else:
                ts_dict[value] = key
            
        return True
