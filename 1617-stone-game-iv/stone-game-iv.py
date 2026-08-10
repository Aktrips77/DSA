class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] stores whether the current player can win with 'i' stones
        dp = [False] * (n + 1)
        
        # Iterate through all stone counts from 1 to n
        for i in range(1, n + 1):
            k = 1
            # Try removing every possible square number k*k
            while k * k <= i:
                # If removing k*k stones forces the opponent into a losing state, 
                # the current player wins.
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check other squares
                k += 1
                
        return dp[n]
