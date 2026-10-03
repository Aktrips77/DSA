class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base boundary for calculating length
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of the opening bracket
            else:
                stack.pop()  # Pop the last matching opening bracket or boundary
                if not stack:
                    # If empty, the current ')' is an unmatched invalid boundary
                    stack.append(i)
                else:
                    # Valid substring found: current index minus the new top of the stack
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
