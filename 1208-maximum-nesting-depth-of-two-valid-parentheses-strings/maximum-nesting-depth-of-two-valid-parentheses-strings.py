class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Increment depth first because this character initiates a new depth tier
                depth += 1
                ans.append(depth % 2)
            else:
                # Append the parity of the current depth, then decrement for the closing match
                ans.append(depth % 2)
                depth -= 1
                
        return ans
