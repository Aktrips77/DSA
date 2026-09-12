from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store as (left, right, weight, original_index)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
        
        # Sort primarily by start time
        arr.sort()
        starts = [x[0] for x in arr]
        
        # next_idx[i] points to the first interval starting after arr[i] ends
        next_idx = []
        for i in range(n):
            nxt = bisect_left(starts, arr[i][1] + 1)
            next_idx.append(nxt)
            
        # DP table: memo[i][j] = (max_weight, list_of_sorted_indices)
        # We process from right to left (suffix DP)
        memo = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, w, original_id = arr[i]
            nxt = next_idx[i]
            
            for j in range(1, 5):
                # Option 1: Skip interval i
                skip_w, skip_path = memo[i + 1][j]
                
                # Option 2: Take interval i
                next_w, next_path = memo[nxt][j - 1]
                take_w = w + next_w
                take_path = sorted(next_path + [original_id])
                
                # Compare options based on weight maximum, then lexicographical order
                if take_w > skip_w:
                    memo[i][j] = (take_w, take_path)
                elif skip_w > take_w:
                    memo[i][j] = (skip_w, skip_path)
                else:
                    # Weights are equal; pick the lexicographically smaller path
                    if take_path < skip_path:
                        memo[i][j] = (take_w, take_path)
                    else:
                        memo[i][j] = (skip_w, skip_path)
                        
        return memo[0][4][1]
