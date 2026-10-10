class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        
        # 1. Calculate absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(diffs)
        
        # If total differences are less than or equal to budget, we can make everything 0
        if sum(diffs) <= k:
            return 0
        
        # 2. Populate the frequency bucket array
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
            
        # 3. Greedily push down the largest differences
        for d in range(max_diff, 0, -1):
            if bucket[d] == 0:
                continue
                
            # Determine how many elements we can reduce
            # We can either reduce all elements at this difference level, or as many as k allows
            take = min(bucket[d], k)
            
            bucket[d] -= take
            bucket[d - 1] += take
            k -= take
            
            # If the budget is exhausted, stop processing
            if k == 0:
                break
                
        # 4. Calculate the minimum sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if bucket[d] > 0:
                ans += bucket[d] * (d ** 2)
                
        return ans
