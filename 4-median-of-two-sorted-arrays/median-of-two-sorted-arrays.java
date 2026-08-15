class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the shorter array to optimize runtime to O(log(min(M, N)))
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int low = 0, high = m;
        
        while (low <= high) {
            int i = (low + high) / 2;
            int j = (m + n + 1) / 2 - i;
            
            // Boundary edge cases handling using infinity
            int maxLeftX = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
            int minRightX = (i == m) ? Integer.MAX_VALUE : nums1[i];
            
            int maxLeftY = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
            int minRightY = (j == n) ? Integer.MAX_VALUE : nums2[j];
            
            // Valid partition achieved
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((m + n) % 2 == 0) {
                    return ((double)Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2.0;
                } else {
                    return (double)Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                high = i - 1; // Move left in nums1
            } else {
                low = i + 1;  // Move right in nums1
            }
        }
        
        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}
