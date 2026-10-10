class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # If we need an odd number of ')', the previous '(' needs a pair right now
                if needed_right % 2 == 1:
                    insertions += 1  # Insert a ')'
                    needed_right -= 1 # We fulfilled that single missing ')'
                needed_right += 2
            else:
                # We found a ')'
                # Check if it forms a consecutive pair '}}'
                if i + 1 < n and s[i + 1] == ')':
                    i += 1 # Consume the second ')'
                else:
                    insertions += 1 # Missing a matching consecutive ')' -> Insert one!
                
                # Now match this pair with an open '('
                if needed_right > 0:
                    needed_right -= 2
                else:
                    insertions += 1 # No '(' available -> Insert a '('
            i += 1
            
        return insertions + needed_right
