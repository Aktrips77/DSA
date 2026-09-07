class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # endsIn[i] stores the number of distinct subsequences ending with character i
        endsIn = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # The new value is the sum of all existing subsequences + 1 (for the char itself)
            endsIn[idx] = (sum(endsIn) + 1) % MOD
            
        return sum(endsIn) % MOD
