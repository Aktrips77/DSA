class Solution {
    public int findDuplicate(int[] nums) {
        // Step 1: Detect intersection point using the array as a linked list
        int slow = nums[0];
        int fast = nums[0];
        
        do {
            slow = nums[slow];          // slow = slow.next
            fast = nums[nums[fast]];    // fast = fast.next.next
        } while (slow != fast);
        
        // Step 2: Find the entrance to the cycle (the duplicate number)
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];          // slow = slow.next
            fast = nums[fast];          // fast = fast.next
        }
        
        return slow;
    }
}
