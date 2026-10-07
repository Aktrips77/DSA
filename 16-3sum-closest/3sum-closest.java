import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums); 
        int n = nums.length;
        
        // Ek variable jo pure process mein sabse closest sum ko yaad rakhega
        int closestSum = nums[0] + nums[1] + nums[2]; 

        for(int i = 0; i < n - 2; i++){
            int left = i + 1;
            int right = n - 1;
            
            // Aapki approach: in do pointers ke liye required sum ye hona chahiye
            int requiredSum = target - nums[i]; 
            
            while(left < right){
                // Current pointers ka sum
                int currentTwoSum = nums[left] + nums[right];
                
                // Teeno elements ka total sum
                int currentTripletSum = nums[i] + currentTwoSum;
                
                // Agar current triplet sum target ke zyada paas hai, toh update karein
                if (Math.abs(target - currentTripletSum) < Math.abs(target - closestSum)) {
                    closestSum = currentTripletSum;
                }
                
                // Aapki logic ke hisaab se pointers ko move karna:
                if (currentTwoSum < requiredSum) {
                    // Agar dono pointers ka sum required sum se chhota hai, toh left ko badhao (kyunki array sorted hai)
                    left++;
                } else if (currentTwoSum > requiredSum) {
                    // Agar dono pointers ka sum required sum se bada hai, toh right ko ghatao
                    right--;
                } else {
                    // Agar exact match mil gaya (currentTwoSum == requiredSum), toh wahi best answer hai
                    return target; 
                }
            }
        }
        
        return closestSum;
    }
}