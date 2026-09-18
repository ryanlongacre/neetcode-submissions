class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache: 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.prev.next.prev = node.prev 
    
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right


    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        temp = Node(key, value)
        if key in self.cache.keys():
            self.remove(self.cache[key])
        
        self.insert(temp)
        self.cache[key] = temp

        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)

        
        return
