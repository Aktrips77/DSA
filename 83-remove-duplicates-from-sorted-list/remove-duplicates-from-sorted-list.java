class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // Fix: Added safety check to handle empty lists or single-node lists
        if (head == null) return null; 
        
        ListNode temp = head;
        // Fix: Loop runs only if there is a next node to compare with
        while (temp != null && temp.next != null) { 
            if (temp.next.val == temp.val) {
                temp.next = temp.next.next; // Skip duplicate
            } else {
                temp = temp.next; // Move forward only if no duplicate was removed
            }
        }
        return head;
    }
}
