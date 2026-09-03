class Solution {
    public boolean uniformArray(int[] nums1) {
        int minOdd = Integer.MAX_VALUE;
        
        // Step 1: Find the minimum odd element
        for (int x : nums1) {
            if (x % 2 != 0) {
                minOdd = Math.min(minOdd, x);
            }
        }
        
        // If no odd numbers exist, array can remain uniformly even
        if (minOdd == Integer.MAX_VALUE) {
            return true;
        }
        
        // Step 2: Ensure no even element is smaller than our minimum odd element
        for (int x : nums1) {
            if (x % 2 == 0 && x < minOdd) {
                return false;
            }
        }
        
        return true;
    }
}
