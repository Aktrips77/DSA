class Solution:
    def firstMissingPositive(self, nums):
        
        nums = set(nums)
        i = 1
        
        while True:
            if i not in nums:
                return i
            i += 1