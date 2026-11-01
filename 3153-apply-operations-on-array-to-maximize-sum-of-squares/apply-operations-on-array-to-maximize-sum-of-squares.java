import java.util.*;

class Solution {
    public int maxSum(List<Integer> nums, int k) {
        long MOD = 1_000_000_007L;
        int[] bitCounts = new int[32];
        
        // Count total set bits for each column position
        for (int num : nums) {
            for (int i = 0; i < 32; i++) {
                if (((num >> i) & 1) == 1) {
                    bitCounts[i]++;
                }
            }
        }
        
        long totalSumSquares = 0;
        
        // Greedily reconstruct the k largest numbers
        for (int step = 0; step < k; step++) {
            long currentNum = 0;
            for (int i = 0; i < 32; i++) {
                if (bitCounts[i] > 0) {
                    currentNum |= (1L << i);
                    bitCounts[i]--;
                }
            }
            totalSumSquares = (totalSumSquares + (currentNum * currentNum)) % MOD;
        }
        
        return (int) totalSumSquares;
    }
}
