class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self):
        if self.tail.prev == self.head:
            return None
        last = self.tail.prev
        self.remove(last)
        return last


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.key_map = {}      # key → node
        self.freq_map = {}     # freq → DLL

    def update_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if freq == self.minFreq and self.freq_map[freq].head.next == self.freq_map[freq].tail:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLL()

        self.freq_map[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self.update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self.update_freq(node)
        else:
            if len(self.key_map) >= self.cap:
                lfu_list = self.freq_map[self.minFreq]
                node_to_remove = lfu_list.remove_last()
                del self.key_map[node_to_remove.key]

            new_node = Node(key, value)
            self.key_map[key] = new_node

            if 1 not in self.freq_map:
                self.freq_map[1] = DLL()

            self.freq_map[1].insert(new_node)
            self.minFreq = 1