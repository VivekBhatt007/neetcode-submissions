# class Node:
#     def __init__(self, key, val) :
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left

#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.cap:
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        self.q.remove(key)
        self.q.appendleft(key)
        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.q.remove(key)
        self.q.appendleft(key)
        self.mp[key] = value

        if len(self.q) > self.cap:
            self.mp.pop(self.q.pop())






















        
