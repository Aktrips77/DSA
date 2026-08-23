class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_sum, right_sum = 0, 0
        left_q, right_q = 0, 0
        
        # Process the left half
        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        # Process the right half
        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        # Bob wins if the balanced 4.5 expectation equation holds true
        # Rearranged to avoid floating point operations:
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)
