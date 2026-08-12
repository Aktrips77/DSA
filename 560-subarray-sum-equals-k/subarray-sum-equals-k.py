class Solution:
    def subarraySum(self, nums, k):
        
        from collections import defaultdict
        
        count = 0
        prefix = 0
        hashmap = defaultdict(int)
        
        hashmap[0] = 1
        
        for num in nums:
            
            prefix += num
            
            if prefix - k in hashmap:
                count += hashmap[prefix-k]
            
            hashmap[prefix] += 1
        
        return count 