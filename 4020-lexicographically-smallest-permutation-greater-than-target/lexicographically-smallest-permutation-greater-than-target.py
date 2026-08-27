from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Step 1: Match target characters as far as possible from left to right
        matched_len = 0
        for i in range(n):
            if counts[target[i]] > 0:
                counts[target[i]] -= 1
                matched_len += 1
            else:
                break
                
        # Step 2: Backtrack right-to-left to find the optimal breaking pivot position
        for i in range(matched_len, -1, -1):
            if i < n:
                # Search for the absolute smallest character strictly larger than target[i]
                target_char_code = ord(target[i])
                chosen_char = None
                
                for offset in range(1, 26):
                    next_char = chr(target_char_code + offset)
                    if counts[next_char] > 0:
                        chosen_char = next_char
                        break
                        
                if chosen_char:
                    # Construct valid prefix matched up to i-1 + the next larger character
                    prefix = list(target[:i]) + [chosen_char]
                    counts[chosen_char] -= 1
                    
                    # Suffix positions are filled greedily with remaining items in sorted order
                    suffix = []
                    for code in range(97, 123):  # 'a' to 'z'
                        char = chr(code)
                        if counts[char] > 0:
                            suffix.extend([char] * counts[char])
                            
                    return "".join(prefix + suffix)
            
            # Reclaim character state for preceding positional checks
            if i > 0:
                counts[target[i - 1]] += 1
                
        return ""
