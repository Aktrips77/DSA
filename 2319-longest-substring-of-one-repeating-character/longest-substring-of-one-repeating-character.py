class Node:
    def __init__(self, start, end, char=None):
        self.start = start
        self.end = end
        # Leftmost and rightmost characters of this range
        self.lc = char
        self.rc = char
        # Maximum lengths of repeating character sequences
        self.lmx = 1  # From left boundary
        self.rmx = 1  # From right boundary
        self.mx = 1   # Absolute max within range

class SegmentTree:
    def __init__(self, s: str):
        self.s = list(s)
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self._build(0, 0, self.n - 1)
        
    def _merge_nodes(self, parent: Node, left: Node, right: Node):
        parent.lc = left.lc
        parent.rc = right.rc
        parent.lmx = left.lmx
        parent.rmx = right.rmx
        parent.mx = max(left.mx, right.mx)
        
        # If the crossing point has matching characters, merge across the boundary
        if left.rc == right.lc:
            parent.mx = max(parent.mx, left.rmx + right.lmx)
            
            # Left prefix expands all the way into the right child
            if left.lmx == (left.end - left.start + 1):
                parent.lmx = left.lmx + right.lmx
                
            # Right suffix expands all the way into the left child
            if right.rmx == (right.end - right.start + 1):
                parent.rmx = right.rmx + left.rmx

    def _build(self, node_idx, start, end):
        if start == end:
            self.tree[node_idx] = Node(start, end, self.s[start])
            return
            
        mid = (start + end) // 2
        left_child = 2 * node_idx + 1
        right_child = 2 * node_idx + 2
        
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        
        self.tree[node_idx] = Node(start, end)
        self._merge_nodes(self.tree[node_idx], self.tree[left_child], self.tree[right_child])

    def update(self, node_idx, target_idx, char):
        node = self.tree[node_idx]
        if node.start == node.end == target_idx:
            node.lc = node.rc = char
            return
            
        mid = (node.start + node.end) // 2
        left_child = 2 * node_idx + 1
        right_child = 2 * node_idx + 2
        
        if target_idx <= mid:
            self.update(left_child, target_idx, char)
        else:
            self.update(right_child, target_idx, char)
            
        self._merge_nodes(node, self.tree[left_child], self.tree[right_child])

    def get_max_length(self):
        return self.tree[0].mx


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        tree = SegmentTree(s)
        results = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(0, idx, char)
            results.append(tree.get_max_length())
            
        return results
