class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If the total number of '1's is less than k, no valid substring exists
        if s.count('1') < k:
            return ""
            
        ans = ""
        l = 0
        ones_count = 0
        
        for r in range(len(s)):
            if s[r] == '1':
                ones_count += 1
                
            # When we have exactly k '1's, shrink the left to optimize length
            while ones_count == k:
                # Remove leading zeros to find the true structural start of the beautiful block
                if s[l] == '1':
                    current_str = s[l : r + 1]
                    
                    # Update ans if it's empty, shorter, or lexicographically smaller
                    if not ans or len(current_str) < len(ans):
                        ans = current_str
                    elif len(current_str) == len(ans) and current_str < ans:
                        ans = current_str
                        
                    ones_count -= 1
                l += 1
                
        return ans
