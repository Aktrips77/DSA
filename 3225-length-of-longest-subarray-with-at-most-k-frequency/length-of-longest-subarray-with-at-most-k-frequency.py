class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        frequency = {}
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Add current element to the frequency map
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1
            
            # Shrink window from the left if frequency exceeds k
            while frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
                
            # Update the maximum valid window size
            max_length = max(max_length, right - left + 1)
            
        return max_length
