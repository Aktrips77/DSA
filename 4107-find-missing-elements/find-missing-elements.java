
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }

        // 1. Find min and max values safely
        int min = nums[0];
        int max = nums[0];
        Set<Integer> numSet = new HashSet<>();
        
        for (int num : nums) {
            if (num < min) min = num;
            if (num > max) max = num;
            numSet.add(num); // Store elements for O(1) lookup
        }

        // 2. Identify missing elements in the range [min, max]
        for (int i = min; i <= max; i++) {
            if (!numSet.contains(i)) {
                result.add(i);
            }
        }

        return result;
    }
}
