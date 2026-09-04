class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            
            // 1. 0 se lekar i tak ka Maximum element dhundo
            int maxVal = nums[0];
            for (int j = 0; j <= i; j++) {
                if (nums[j] > maxVal) {
                    maxVal = nums[j];
                }
            }
            
            // 2. i se lekar end (n-1) tak ka Minimum element dhundo
            int minVal = nums[i];
            for (int j = i; j < n; j++) {
                if (nums[j] < minVal) {
                    minVal = nums[j];
                }
            }
            
            // 3. Score nikalo (Max - Min)
            int insc = maxVal - minVal;
            
            // 4. Agar score <= k hai, toh yahi index answer hai
            if (insc <= k) {
                return i;
            }
        }
        
        return -1;
    }
}