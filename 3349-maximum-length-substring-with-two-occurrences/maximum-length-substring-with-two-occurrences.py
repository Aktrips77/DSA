class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        ans = 0
        l = 0
        
        for r in range(len(s)):
            idx = ord(s[r]) - ord('a')
            count[idx] += 1
            
            while count[idx] > 2:
                count[ord(s[l]) - ord('a')] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
            
        return ans


