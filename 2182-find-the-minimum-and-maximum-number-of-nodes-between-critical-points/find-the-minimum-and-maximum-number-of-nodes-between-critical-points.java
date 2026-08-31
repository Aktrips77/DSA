/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return new int[]{-1, -1};
        }

        int firstCp = -1;
        int prevCp = -1;
        
        int minDist = Integer.MAX_VALUE;
        int maxDist = -1;
        
        int currIdx = 1;
        ListNode prev = head;
        ListNode curr = head.next;
        
        while (curr.next != null) {
            ListNode nxt = curr.next;
            
            boolean isMaxima = curr.val > prev.val && curr.val > nxt.val;
            boolean isMinima = curr.val < prev.val && curr.val < nxt.val;
            
            if (isMaxima || isMinima) {
                if (firstCp == -1) {
                    firstCp = currIdx;
                } else {
                    minDist = Math.min(minDist, currIdx - prevCp);
                    maxDist = currIdx - firstCp;
                }
                prevCp = currIdx;
            }
            
            prev = curr;
            curr = nxt;
            currIdx++;
        }
        
        if (maxDist == -1) {
            return new int[]{-1, -1};
        }
        
        return new int[]{minDist, maxDist};
    }
}
