import java.util.ArrayList;
import java.util.List;

class Solution {
    // Your sorting function
    int[] sortarr(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] < nums[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        return nums;
    }

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // 1. Pehle array ko sort karo
        sortarr(nums);
        
        // 2. Ek number ko fix karne ke liye loop chalao (fixed = nums[i])
        for (int i = 0; i < nums.length - 2; i++) {
            
            // Duplicate elements ko skip karo takis unique triplets milein
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // 3. Baaki bache do numbers ke liye 2 pointers set karo
            int left = i + 1; 
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    // Triplet mil gaya! Result me add karo
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[left]);
                    triplet.add(nums[right]);
                    result.add(triplet);
                    
                    // Left aur Right ke duplicates ko bhi skip karo
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Pointers ko aage badhao
                    left++;
                    right--;
                } 
                else if (sum < 0) {
                    // Agar sum chota hai, toh left pointer ko right me shift karo (bada number chahiye)
                    left++;
                } 
                // Agar sum bada hai, toh right pointer ko left me shift karo (chota number chahiye)
                else {
                    right--;
                }
            }
        }
        
        return result;
    }
}
