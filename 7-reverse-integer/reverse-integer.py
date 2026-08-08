class Solution:
    def reverse(self, x: int) -> int:
        # Convert to string
        s = str(x)
        
        # If negative, reverse everything after the '-' and put the '-' back in front
        if s[0] == '-':
            reversed_int = int('-' + s[1:][::-1])
        else:
            reversed_int = int(s[::-1])
            
        # LeetCode 32-bit integer overflow check
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int
