class MyHashSet(object):

    def __init__(self):
        self.MyHashSet = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.MyHashSet.add(key)

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.MyHashSet.discard(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.MyHashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)