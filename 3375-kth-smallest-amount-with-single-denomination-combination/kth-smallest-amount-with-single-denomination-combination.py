import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Precompute the LCM for every non-empty subset of coins
        # to avoid recalculating them inside the binary search loop.
        n = len(coins)
        subset_lcm = []
        
        # 1 << n gives total combinations (2^n)
        for i in range(1, 1 << n):
            current_lcm = 1
            count = 0
            for j in range(n):
                if (i >> j) & 1:
                    # Calculate LCM using GCD: (a * b) // gcd(a, b)
                    current_lcm = (current_lcm * coins[j]) // math.gcd(current_lcm, coins[j])
                    count += 1
            # Store (LCM value, size of subset)
            subset_lcm.append((current_lcm, count))
            
        # Helper function to count how many multiples exist <= mid
        def count_multiples(mid: int) -> int:
            total = 0
            for lcm_val, count in subset_lcm:
                if count % 2 == 1:
                    total += mid // lcm_val
                else:
                    total -= mid // lcm_val
            return total

        # Binary search for the exact kth value
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the boundary
                
        return ans
