class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        d= str(digit)
        ans=0
        for num in nums:
            ans +=str(num).count(d)
        return ans
        
        