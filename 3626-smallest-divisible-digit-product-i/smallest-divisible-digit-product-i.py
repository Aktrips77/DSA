class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # Calculate the product of digits
            digit_product = 1
            temp = n
            
            while temp > 0:
                digit_product *= (temp % 10)
                temp //= 10
            
            # Check divisibility
            if digit_product % t == 0:
                return n
            
            n += 1
