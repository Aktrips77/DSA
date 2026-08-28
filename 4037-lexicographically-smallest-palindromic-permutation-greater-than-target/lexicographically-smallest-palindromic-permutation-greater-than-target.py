from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        global_counts = Counter(s)
        
        # 1. Palindrome structural validity check
        odd_chars = [c for c, freq in global_counts.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        half_len = (n + 1) // 2
        candidates = []
        
        # 2. Iterate through every possible prefix match length 'i'
        for i in range(half_len + 1):
            pool = global_counts.copy()
            left_arr = []
            possible = True
            
            # Match the target characters exactly up to index i - 1
            for j in range(i):
                c = target[j]
                # Each placement in the left half requires 2 characters (or 1 if it's the exact middle slot)
                needed = 1 if (n % 2 != 0 and j == half_len - 1) else 2
                if pool[c] >= needed:
                    pool[c] -= needed
                    left_arr.append(c)
                else:
                    possible = False
                    break
                    
            if not possible:
                continue
                
            # If we matched the entire first half perfectly, build and test it directly
            if i == half_len:
                # Reconstruct mid character if odd length
                current_mid = mid_char if n % 2 != 0 else ""
                left_str = "".join(left_arr)
                
                # If it's an odd length, the last character of left_arr is technically the middle slot
                if n % 2 != 0 and left_arr:
                    pal = "".join(left_arr[:-1]) + left_arr[-1] + "".join(left_arr[:-1])[::-1]
                else:
                    pal = left_str + left_str[::-1]
                    
                if pal > target:
                    candidates.append(pal)
                continue
                
            # Otherwise, at index i, choose a character strictly larger than target[i]
            needed_for_chosen = 1 if (n % 2 != 0 and i == half_len - 1) else 2
            for chosen in sorted(pool.keys()):
                if chosen > target[i] and pool[chosen] >= needed_for_chosen:
                    curr_pool = pool.copy()
                    curr_pool[chosen] -= needed_for_chosen
                    
                    # Create the branch left half
                    branch_left = left_arr + [chosen]
                    
                    # Fill the rest of the first half greedily with the smallest available characters
                    for pos in range(i + 1, half_len):
                        req = 1 if (n % 2 != 0 and pos == half_len - 1) else 2
                        for c in sorted(curr_pool.keys()):
                            if curr_pool[c] >= req:
                                curr_pool[c] -= req
                                branch_left.append(c)
                                break
                                
                    # Extract the standalone center character if it exists
                    branch_mid = ""
                    if n % 2 != 0:
                        branch_mid = branch_left.pop()
                        
                    # Build full palindrome structure
                    l_str = "".join(branch_left)
                    pal = l_str + branch_mid + l_str[::-1]
                    
                    if pal > target:
                        candidates.append(pal)
                        
        return min(candidates) if candidates else ""
