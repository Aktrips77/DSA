from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: Subarrays of length 1
        if k == 1:
            ans = -1
            for num, count in counts.items():
                if count == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 2: Only one subarray of length N
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        # Only the first or last elements can be part of exactly one window
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[n - 1]] == 1:
            ans = max(ans, nums[n - 1])
            
        return ans
