class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.cache = {}

        #create dummy head and tail consisting LRU and MRU
        self.head = Node(0,0)
        self.tail = Node(0,0)

        #linking head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # helper funct 1: remove the node
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        #combine these two nodes
        prev_node.next = next_node
        next_node.prev = prev_node

    # helper function 2: add the node to the MRU part
    def _add(self, node):
        prev_node =self.tail.prev

        # relation of prev_node with new node
        node.prev = prev_node
        prev_node.next =node

        #relation of node with tail
        node.next = self.tail
        self.tail.prev = node 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            self._add(node)
            return node.value
        return -1
      

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key,value)
        self._add(new_node)
        self.cache[key]=new_node

        # check capacity

        if len(self.cache)> self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)