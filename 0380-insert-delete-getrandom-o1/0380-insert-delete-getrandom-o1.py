import random

class RandomizedSet(object):

    def __init__(self):
       self.val = set() 

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
    
        if val in self.val:
            return False
        
        self.val.add(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val:
            return False
        
        self.val.remove(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.val))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()