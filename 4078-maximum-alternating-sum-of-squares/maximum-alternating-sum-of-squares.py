class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Step 1: Convert all elements to their squares and sort
        squares = sorted(x * x for x in nums)
        
        # Step 2: The first floor(n // 2) elements will be subtracted
        mid = len(squares) // 2
        
        # Step 3: Return sum of the upper half minus the lower half
        return sum(squares[mid:]) - sum(squares[:mid])
