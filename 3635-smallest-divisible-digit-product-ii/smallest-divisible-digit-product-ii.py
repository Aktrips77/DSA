class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        PRIMES = [2, 3, 5, 7]
        
        # factor_counts[digit] = [count_of_2, count_of_3, count_of_5, count_of_7]
        FACTOR_COUNTS = [
           [0, 0, 0, 0], # 0 (unused)
           [0, 0, 0, 0], # 1
           [1, 0, 0, 0], # 2
           [0, 1, 0, 0], # 3
           [2, 0, 0, 0], # 4
           [0, 0, 1, 0], # 5
           [1, 1, 0, 0], # 6
           [0, 0, 0, 1], # 7
           [3, 0, 0, 0], # 8
           [0, 2, 0, 0]  # 9
        ]
        
        # Step 1: Extract prime factors of t
        target_factors = [0] * 4
        temp_t = t
        for i, prime in enumerate(PRIMES):
            while temp_t % prime == 0:
                target_factors[i] += 1
                temp_t //= prime
                
        # If t has prime factors other than 2, 3, 5, 7, it's impossible
        if temp_t > 1:
            return "-1"
            
        n = len(num)
        digits = [int(c) for c in num]
        
        # Track required prime factors at each position index
        required_at_pos = [[0] * 4 for _ in range(n + 1)]
        required_at_pos[0] = list(target_factors)
        
        def get_min_length(factors):
            """Calculates min digits needed to satisfy remaining prime factors."""
            f2, f3, f5, f7 = factors
            
            c8, f2 = divmod(f2, 3)
            c9, f3 = divmod(f3, 2)
            
            c6 = 0
            if f2 > 0 and f3 > 0:
                c6 = 1
                f2 -= 1
                f3 -= 1
                
            c4, f2 = divmod(f2, 2)
            c2, c3 = f2, f3
            
            return c8 + c9 + c6 + c4 + c2 + c3 + f5 + f7

        def build_suffix(factors, total_length):
            """Generates the lexicographically smallest suffix of total_length."""
            f2, f3, f5, f7 = factors
            
            c8, f2 = divmod(f2, 3)
            c9, f3 = divmod(f3, 2)
            
            c6 = 0
            if f2 > 0 and f3 > 0:
                c6 = 1
                f2 -= 1
                f3 -= 1
                
            c4, f2 = divmod(f2, 2)
            c2, c3 = f2, f3
            
            digit_count = c2 + c3 + c4 + f5 + c6 + f7 + c8 + c9
            ones = total_length - digit_count
            
            return (
                "1" * ones +
                "2" * c2 +
                "3" * c3 +
                "4" * c4 +
                "5" * f5 +
                "6" * c6 +
                "7" * f7 +
                "8" * c8 +
                "9" * c9
            )

        # Step 2: Try to match the prefix of num as far as possible
        match_len = 0
        while match_len < n:
            curr_digit = digits[match_len]
            if curr_digit == 0:
                break  # 0 cannot be matched, must break and change this position
                
            next_factors = [
                max(0, required_at_pos[match_len][i] - FACTOR_COUNTS[curr_digit][i])
                for i in range(4)
            ]
            
            # Check if suffix length can support the remaining factors
            if get_min_length(next_factors) <= n - 1 - match_len:
                required_at_pos[match_len + 1] = next_factors
                match_len += 1
            else:
                break

        # FIXED: Check if the number itself already works!
        if match_len == n and sum(required_at_pos[n]) == 0:
            return num

        # Step 3: Backtrack and find the first position to safely increment
        # If match_len == n, we can't increment digit at index n, so start backtracking from n-1
        start_idx = match_len - 1 if match_len == n else match_len
        for i in range(start_idx, -1, -1):
            start_digit = digits[i] + 1
            
            for d in range(start_digit, 10):
                next_factors = [
                    max(0, required_at_pos[i][p] - FACTOR_COUNTS[d][p])
                    for p in range(4)
                ]
                
                remaining_len = n - 1 - i
                if get_min_length(next_factors) <= remaining_len:
                    # Construct matching prefix + new digit + greedy suffix
                    prefix = "".join(map(str, digits[:i])) + str(d)
                    suffix = build_suffix(next_factors, remaining_len)
                    return prefix + suffix

        # Step 4: If no solution exists with length n, increase string length
        new_len = max(n + 1, get_min_length(target_factors))
        return build_suffix(target_factors, new_len)
