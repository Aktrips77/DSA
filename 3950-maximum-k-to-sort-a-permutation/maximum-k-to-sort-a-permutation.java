class Solution {
    public int sortPermutation(int[] nums) {
        boolean isSorted = true;
        
        // Check karein ki array pehle se sorted hai ya nahi
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                isSorted = false;
                break;
            }
        }
        
        // Agar pehle se sorted hai, toh answer 0 hoga
        if (isSorted) {
            return 0;
        }
        
        // k ko -1 (yaani saare bits 1) se initialize karein
        int k = -1; 
        
        // Saare misplaced elements ka bitwise AND lein
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                k &= nums[i];
            }
        }
        
        return k;
    }
}
