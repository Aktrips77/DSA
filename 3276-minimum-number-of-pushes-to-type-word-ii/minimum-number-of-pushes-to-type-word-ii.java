import java.util.Arrays;

public class Solution {
    public int minimumPushes(String word) {
        // Step 1: Count the frequency of each lowercase English letter
        int[] frequencies = new int[26];
        for (char c : word.toCharArray()) {
            frequencies[c - 'a']++;
        }
        
        // Step 2: Sort frequencies in ascending order
        Arrays.sort(frequencies);
        
        int totalPushes = 0;
        int distinctCount = 0;
        
        // Step 3: Iterate backwards from the highest frequency
        for (int i = 25; i >= 0; i--) {
            if (frequencies[i] == 0) {
                break; // No more unique letters left
            }
            
            // Calculate keypress cost based on placement layer
            // First 8 distinct letters cost 1 push, next 8 cost 2, etc.
            int pushCost = (distinctCount / 8) + 1;
            totalPushes += frequencies[i] * pushCost;
            
            distinctCount++;
        }
        
        return totalPushes;
    }
}
