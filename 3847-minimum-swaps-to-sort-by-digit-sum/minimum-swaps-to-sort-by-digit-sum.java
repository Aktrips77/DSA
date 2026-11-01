import java.util.*;

class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        
        // Element structure to preserve original index positions
        Element[] arr = new Element[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new Element(nums[i], i, getDigitSum(nums[i]));
        }
        
        // Sort using custom comparator rules (Digit Sum first, then value)
        Arrays.sort(arr, (a, b) -> {
            if (a.digitSum != b.digitSum) {
                return Integer.compare(a.digitSum, b.digitSum);
            }
            return Integer.compare(a.val, b.val);
        });
        
        boolean[] visited = new boolean[n];
        int swaps = 0;
        
        // Count cycle sizes to compute minimum swaps
        for (int i = 0; i < n; i++) {
            if (visited[i] || arr[i].initIdx == i) {
                continue;
            }
            
            int cycleSize = 0;
            int curr = i;
            while (!visited[curr]) {
                visited[curr] = true;
                curr = arr[curr].initIdx;
                cycleSize++;
            }
            
            if (cycleSize > 0) {
                swaps += (cycleSize - 1);
            }
        }
        
        return swaps;
    }
    
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
    
    private static class Element {
        int val;
        int initIdx;
        int digitSum;
        
        Element(int val, int initIdx, int digitSum) {
            this.val = val;
            this.initIdx = initIdx;
            this.digitSum = digitSum;
        }
    }
}
