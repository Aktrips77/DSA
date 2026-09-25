from collections import deque

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Queue initialized with the original expression string
        queue = deque([expression])
        res = set()
        
        while queue:
            curr = queue.popleft()
            
            # Find the first closing brace
            r = curr.find('}')
            
            # Base case: no braces left, add to the final set
            if r == -1:
                res.add(curr)
                continue
                
            # Find the closest matching opening brace to its left
            l = curr.rfind('{', 0, r)
            
            # Split the inner expression by comma
            prefix = curr[:l]
            suffix = curr[r+1:]
            options = curr[l+1:r].split(',')
            
            # Enqueue all variations back into the queue
            for option in options:
                queue.append(prefix + option + suffix)
                
        # Return sorted deduplicated results
        return sorted(list(res))
