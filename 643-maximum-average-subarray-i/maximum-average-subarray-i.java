class Solution {
    public double findMaxAverage(int[] nums, int k) {
         double sumavg=0;
         // first window  for average k tak chalegi
         for(int i=0;i<k;i++){
            sumavg=(sumavg+nums[i]); 
         }
         double maxavg=sumavg;

         // sliding window 
         for ( int j=k;j<nums.length;j++){
              sumavg= (sumavg-nums[j-k]+ nums[j]);

              maxavg=Math.max(sumavg,maxavg);
         }

         return maxavg/k; // avg last me kar de naa loop me har step calculate hoti hain 
    }
}