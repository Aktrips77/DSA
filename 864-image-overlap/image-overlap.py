from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        # Collect coordinates of all 1s
        ones1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        ones2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        # Count frequencies of displacement vectors
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_vector = (r1 - r2, c1 - c2)
                shift_counts[shift_vector] += 1
                max_overlap = max(max_overlap, shift_counts[shift_vector])
                
        return max_overlap
