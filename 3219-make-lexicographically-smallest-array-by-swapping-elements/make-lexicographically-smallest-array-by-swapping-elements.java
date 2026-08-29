import java.util.*;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[][] paired = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            paired[i][0] = nums[i];
            paired[i][1] = i;
        }
        
        // Sort pairs primarily by their numerical value
        Arrays.sort(paired, (a, b) -> Integer.compare(a[0], b[0]));
        
        int[] result = new int[n];
        int i = 0;
        
        while (i < n) {
            int j = i + 1;
            while (j < n && paired[j][0] - paired[j - 1][0] <= limit) {
                j++;
            }
            
            // Collect indices for the current transitive group
            int[] indices = new int[j - i];
            for (int k = i; k < j; k++) {
                indices[k - i] = paired[k][1];
            }
            Arrays.sort(indices);
            
            // Map sorted elements back to chronological position slots
            for (int k = i; k < j; k++) {
                result[indices[k - i]] = paired[k][0];
            }
            
            i = j;
        }
        
        return result;
    }
}
