class Solution {
    public int countCommas(int n) {
        // If n is less than 1000, no numbers contain any commas.
        if (n < 1000) {
            return 0;
        }
        
        // Every number from 1000 to n contains exactly 1 comma.
        return n - 999;
    }
}
