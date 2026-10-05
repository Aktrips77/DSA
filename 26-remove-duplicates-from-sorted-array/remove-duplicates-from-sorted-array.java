class Solution {
    public int removeDuplicates(int[] nums) {
        // Handle edge case for empty array (though constraints say length >= 1)
        if (nums.length == 0) {
            return 0;
        }
        
        // 'slow' pointer keeps track of the index for the next unique element
        int slow = 0;
        
        // 'fast' pointer iterates through the array to find unique elements
        for (int fast = 1; fast < nums.length; fast++) {
            // When a new unique element is found
            if (nums[fast] != nums[slow]) {
                slow++; // Move the slow pointer forward by 1
                nums[slow] = nums[fast]; // Overwrite the duplicate in-place
            }
        }
        
        // 'slow' is a 0-based index, so adding 1 gives the total count of unique elements
        return slow + 1;
    }
}