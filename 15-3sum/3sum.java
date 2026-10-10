import java.util.ArrayList;
import java.util.List;

class Solution {

    

    public List<List<Integer>> threeSum(int[] nums) {
      List<List<Integer>> result = new ArrayList<>();
        // 1.sort array
        java.util.Arrays.sort(nums);

        int n=nums.length;
        for(int i=0;i<n-2;i++){ // for triplet 
        // duplicate check at starting as first will be always unique
        if(i>0 && nums[i]==nums[i-1]){
            continue;
        }
           int left=i+1;
           int right=n-1;
           int target=0+(-1*nums[i]);


           while(left<right){
            int sum=nums[left]+nums[right];
            if(sum==target){
               
               result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                left++;
                right--;

                while(left<n && nums[left]==nums[left-1]){
                   left++;
                }
                while(right>0 && nums[right]==nums[right+1]){
                    right--;
                }
            }
            else if(sum<target){
                left++;
            }
            else{
                right--;
            }
           }

        }

        return result;
    }
}
