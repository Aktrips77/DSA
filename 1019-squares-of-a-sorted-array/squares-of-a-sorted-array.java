import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] nums) {
        int [] result= new int[nums.length];

        // // brute force
        // for(int i=0;i<nums.length;i++){
        //     result[i]=nums[i]*nums[i];
        // }

        // Arrays.sort(result);

        // return result;

        // 2 pointer 
        int left=0;
        int right=nums.length-1;
        int idx=nums.length-1;

        while(left<=right){ // middle element must be processed
        int leftsq=nums[left]*nums[left];
        int rtsq=nums[right]* nums[right];

        if(leftsq>rtsq){
            result[idx]=leftsq;

            left++;

        }
        else{
            result[idx]=rtsq;
            right--;
        }
        idx--;
        }
        return result;

    }
}