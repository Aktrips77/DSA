class LazySegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        val = self.lazy[node]
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        # Update Left Child
        len_l = mid - start + 1
        self.sum_sq[left_child] = (self.sum_sq[left_child] + 2 * val * self.sum[left_child] + val * val % self.MOD * len_l) % self.MOD
        self.sum[left_child] = (self.sum[left_child] + val * len_l) % self.MOD
        self.lazy[left_child] = (self.lazy[left_child] + val) % self.MOD

        # Update Right Child
        len_r = end - mid
        self.sum_sq[right_child] = (self.sum_sq[right_child] + 2 * val * self.sum[right_child] + val * val % self.MOD * len_r) % self.MOD
        self.sum[right_child] = (self.sum[right_child] + val * len_r) % self.MOD
        self.lazy[right_child] = (self.lazy[right_child] + val) % self.MOD

        self.lazy[node] = 0

    def update_range(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        
        if l <= start and end <= r:
            length = end - start + 1
            # (x + val)^2 = x^2 + 2*val*x + val^2
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum[node] + val * val % self.MOD * length) % self.MOD
            self.sum[node] = (self.sum[node] + val * length) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, l, r, val)
        self.update_range(2 * node + 1, mid + 1, end, l, r, val)
        
        self.sum[node] = (self.sum[2 * node] + self.sum[2 * node + 1]) % self.MOD
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = LazySegmentTree(n)
        last_seen = {}
        total_ans = 0

        for r in range(n):
            # Find the boundary for distinct element expansion
            l = last_seen.get(nums[r], -1) + 1
            
            # Increment distinct counts for all subarrays starting between l and r
            tree.update_range(1, 0, n - 1, l, r, 1)
            
            # tree.sum_sq[1] inherently holds the total sum of squares for all valid starting boundaries up to r
            total_ans = (total_ans + tree.sum_sq[1]) % MOD
            
            # Record current position
            last_seen[nums[r]] = r

        return total_ans
