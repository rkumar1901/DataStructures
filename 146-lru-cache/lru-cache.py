class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):

        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_at_end(self,node):

        prev_node = self.tail.prev

        node.next = self.tail
        prev_node.next = node
        node.prev = prev_node
        self.tail.prev = node

    
    def get(self, key):

        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.insert_at_end(node)
        return node.value


    def put(self, key, value):

        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.remove(node)
            self.insert_at_end(node)
            return

        new_node = Node(key,value)
        self.insert_at_end(new_node)
        self.dic[key] = new_node
        
        if len(self.dic) > self.capacity:
            del_node = self.head.next
            self.remove(del_node)
            del self.dic[del_node.key]

            








        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)