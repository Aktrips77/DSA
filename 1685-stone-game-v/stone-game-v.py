class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0

        # Prefix sums
        prefix = [0] * (n + 1)
        for idx, val in enumerate(stoneValue):
            prefix[idx + 1] = prefix[idx] + val

        def get_sum(l: int, r: int) -> int:
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                if mid < i:
                    mid = i

                # Advance mid until left sum exceeds right sum
                while mid < j and (prefix[mid + 1] - prefix[i]) * 2 < (prefix[j + 1] - prefix[i]):
                    mid += 1

                total = prefix[j + 1] - prefix[i]
                ans = 0

                # Case 1: left_sum < right_sum for k in [i, mid - 1]
                if mid > i:
                    ans = max(ans, max_left[i][mid - 1])

                # Case 2: left_sum == right_sum at mid
                if (prefix[mid + 1] - prefix[i]) * 2 == total:
                    ans = max(ans, max_left[i][mid], max_right[mid + 1][j])
                # Case 3: left_sum > right_sum for k in [mid, j - 1]
                elif mid < j:
                    ans = max(ans, max_right[mid + 1][j])

                dp[i][j] = ans
                max_left[i][j] = max(max_left[i][j - 1], total + ans)
                max_right[i][j] = max(max_right[i + 1][j], total + ans)

        return dp[0][n - 1]