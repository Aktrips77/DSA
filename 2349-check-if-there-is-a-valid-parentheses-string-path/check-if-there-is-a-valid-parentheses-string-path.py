class Solution:
    def hasValidPath(self, grid: List[List[char]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        # The path must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(r, c, k):
            # If closed brackets exceed open brackets, this path is invalid
            if k < 0:
                return False
                
            # If we out of bounds, stop
            if r >= m or c >= n:
                return False
                
            # Update balance for the current cell
            k += 1 if grid[r][c] == '(' else -1
            
            # Reached destination: check if balance is perfectly zero
            if r == m - 1 and c == n - 1:
                return k == 0
                
            # Memoization check
            state = (r, c, k)
            if state in memo:
                return memo[state]
                
            # Explore moving right or moving down
            memo[state] = dfs(r + 1, c, k) or dfs(r, c + 1, k)
            return memo[state]

        return dfs(0, 0, 0)
