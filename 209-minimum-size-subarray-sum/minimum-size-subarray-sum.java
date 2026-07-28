class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left=0;  // shrink pointer 
        
         int sum=0;
         int minLength=Integer.MAX_VALUE; // INITIALLY INFINITE HOGI 

         for(int right=0;right<nums.length;right++){  // windows expand
             sum+=nums[right];

             while(sum>=target){
                minLength=Math.min(minLength,right-left+1);
                sum-=nums[left]; // shrinking window
                left++;
                
             }

         }   

            if(minLength == Integer.MAX_VALUE)
                  return 0; // agar kabhi bhi condition satisfy naa ho

        return minLength;
        
    }
}