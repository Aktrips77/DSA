class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Compute prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
            
        # Base case: if the only option left is to take all elements up to index n-1
        # dp stores the rolling optimal state difference (dp[i+1]) moving backwards
        dp = prefix[n - 1]
        
        # Iterate backwards from the second-to-last index down to index 1 (2nd element)
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
            
        return dp
