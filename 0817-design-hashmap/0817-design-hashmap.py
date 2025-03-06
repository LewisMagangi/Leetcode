class MyHashMap(object):

    def __init__(self):
        self.MyHashMap = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.MyHashMap[key] = value
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.MyHashMap.get(key, -1)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.MyHashMap.pop(key, None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)