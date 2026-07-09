class Solution {
    public int[] getConcatenation(int[] nums) {
        
        int [] concnums= new int [2*(nums.length)];
        int l=0;
        int r=nums.length;
        

            for(int i=0; i<nums.length;i++){
                concnums[l]=nums[i];
                l++;
                concnums[r]=nums[i];
                r++;

            }

        

        
        
        return concnums;

    }
}