class Solution {
    int[] returnsq(int [] nums){
        int[] sq=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            sq[i]=nums[i]*nums[i];

        }

        return sq;
    }
    public int[] sortedSquares(int[] nums) {
        int[] sq = returnsq(nums); // calling the function
        for(int i=0;i<sq.length;i++){
            for(int j=0;j<i;j++){
                if (sq[i]<sq[j]){
                    int temp=sq[i];
                    sq[i]=sq[j];
                    sq[j]=temp;
                }
            }
        }
        return sq;
    }
}