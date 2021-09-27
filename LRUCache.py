class LRUCache(object):
    from collections import deque, OrderedDict
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
       

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key in self.cache:
            answer = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = answer
            #print("cache:", self.cache)
            return answer
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if len(self.cache) < self.capacity:
            if key in self.cache:
                self.cache.pop(key)
                
            self.cache[key] = value
            
        else:
            #print("cache:", self.cache)
            if key in self.cache:
                self.cache.pop(key)
            else:
                self.cache.popitem(last=False)
                
            self.cache[key] = value
