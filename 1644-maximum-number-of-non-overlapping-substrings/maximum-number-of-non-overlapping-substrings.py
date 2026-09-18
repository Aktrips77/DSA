class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        # Step 1: Find the absolute first and last index for each character
        left = [n] * 26
        right = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = i
            
        valid_intervals = []
        
        # Step 2: Try to form a valid expanded interval starting at each char's first occurrence
        for i in range(n):
            if i == left[ord(s[i]) - ord('a')]:
                curr_right = right[ord(s[i]) - ord('a')]
                j = i
                is_valid = True
                
                # Dynamically expand the right bound to include all internal characters
                while j <= curr_right:
                    ch_idx = ord(s[j]) - ord('a')
                    # If an inner character started before 'i', this interval cannot start at 'i'
                    if left[ch_idx] < i:
                        is_valid = False
                        break
                    curr_right = max(curr_right, right[ch_idx])
                    j += 1
                
                if is_valid:
                    valid_intervals.append((i, curr_right))
        
        # Step 3: Greedy selection (Sort by end index to maximize non-overlapping choices)
        valid_intervals.sort(key=lambda x: x[1])
        
        ans = []
        last_end = -1
        for start, end in valid_intervals:
            if start > last_end:
                ans.append(s[start : end + 1])
                last_end = end
                
        return ans
