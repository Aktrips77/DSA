from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if not s:
            return [""]
            
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        found = False
        result = []
        
        while queue:
            # Process all nodes at the current removal level
            level_size = len(queue)
            current_level_strings = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if isValid(curr):
                    result.append(curr)
                    found = True
                
                if not found:
                    # Generate all states by removing one parenthesis
                    for i in range(len(curr)):
                        if curr[i] not in ('(', ')'):
                            continue
                        # Create a new string by omitting character at index i
                        next_state = curr[:i] + curr[i+1:]
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
            
            # If valid strings are found at this level, stop going deeper
            if found:
                break
                
        return result
