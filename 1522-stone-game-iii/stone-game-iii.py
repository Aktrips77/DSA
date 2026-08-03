class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # Represents dp[i+1], dp[i+2], dp[i+3] respectively
        next_1, next_2, next_3 = 0, 0, 0
        
        for i in range(n - 1, -1, -1):
            # Option 1: Take 1 stone
            current_margin = stoneValue[i] - next_1
            
            # Option 2: Take 2 stones
            if i + 1 < n:
                current_margin = max(current_margin, stoneValue[i] + stoneValue[i + 1] - next_2)
                
            # Option 3: Take 3 stones
            if i + 2 < n:
                current_margin = max(current_margin, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - next_3)
            
            # Shift variables for the next iteration (moving left)
            next_3 = next_2
            next_2 = next_1
            next_1 = current_margin
            
        if next_1 > 0:
            return "Alice"
        elif next_1 < 0:
            return "Bob"
        return "Tie"
