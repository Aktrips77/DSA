from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # last[j] stores the maximum index in word1 from which 
        # we can form the suffix of word2 starting at index j (exact match)
        last = [-1] * m
        
        # Step 1: Precompute rightmost exact matches from right to left
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        ans = []
        j = 0  # Pointer for word2
        changed = False  # Track if we used our single allowed substitution
        
        # Step 2: Greedy matching from left to right
        for i in range(n):
            if j == m:
                break
                
            # Case A: Characters match identically
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            else:
                # Case B: Mismatch. Can we afford to change this character?
                # We can modify if we haven't changed a character yet AND
                # the remaining suffix of word2 (j+1) can be fully completed by suffix of word1
                if not changed and (j + 1 == m or last[j + 1] > i):
                    ans.append(i)
                    j += 1
                    changed = True  # Consume our 1 allowed character change

        return ans if len(ans) == m else []
