class Solution {
    public int[] runningSum(int[] nums) {
        
        for(int i=1; i< nums.length;i++){ // i=1 not 0 because last index ke aage array chala jaaega , ie out of bound 
            nums[i]=nums[i] + nums[i-1];
        }
        return nums;
        
    }
}