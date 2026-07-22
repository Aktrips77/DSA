class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // if sum< target l++ ; if sum==target return indexes; if sum>target r--;
         int left =0;
         int right=numbers.length-1;
         int n= numbers.length;

         while(left<right){
          int sum= numbers[left] + numbers[right];

          if(sum< target){
            left ++;
          }
          else if( sum==target){
            return new int[] {left +1 , right +1};// index ki value ek aage hain iss question me o/p dekh smjhb jayega

          }

          else{
            right--;
          }
         }
        
       return new int[] {-1,-1};
    }
}
