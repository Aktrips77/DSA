class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int currentNum = nums[i];
            int digitCount = 0;
            
            // Count digits mathematically
            while (currentNum > 0) {
                digitCount++;
                currentNum /= 10;
            }
            
            // Check if digit count is even
            if (digitCount % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}
