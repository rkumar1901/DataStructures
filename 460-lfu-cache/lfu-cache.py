class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self, node):
        # Add to MRU position
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_lru(self):
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.key_to_node = {}
        self.freq_to_list = {}

        self.min_freq = 0

    def get(self, key: int) -> int:

        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # Existing key
        if key in self.key_to_node:

            node = self.key_to_node[key]
            node.value = value

            self._increase_frequency(node)

            return

        # Cache is full
        if self.size == self.capacity:

            lru_list = self.freq_to_list[self.min_freq]

            node = lru_list.remove_lru()

            del self.key_to_node[node.key]

            self.size -= 1

        # New node
        node = Node(key, value)

        self.key_to_node[key] = node

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        self.freq_to_list[1].add(node)

        self.min_freq = 1

        self.size += 1

    def _increase_frequency(self, node):

        old_freq = node.freq

        old_list = self.freq_to_list[old_freq]

        old_list.remove(node)

        # If this was the last node at min frequency
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        node.freq += 1

        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()

        self.freq_to_list[new_freq].add(node)