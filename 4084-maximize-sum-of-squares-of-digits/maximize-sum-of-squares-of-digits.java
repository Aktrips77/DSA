class Solution {
    // Fixed signature: Renamed to maxSumOfSquares to match the driver's template
    public String maxSumOfSquares(int num, int sum) {
        // If the target sum is larger than the maximum possible sum of digits
        if (sum > 9L * num) {
            return "";
        }
        
        int nines = sum / 9;
        int remainder = sum % 9;
        int zeros = num - nines - (remainder > 0 ? 1 : 0);
        
        StringBuilder sb = new StringBuilder();
        
        // Append all the 9s first to make it the largest number possible
        for (int i = 0; i < nines; i++) {
            sb.append('9');
        }
        
        // Append the single leftover remainder digit
        if (remainder > 0) {
            sb.append(remainder);
        }
        
        // Pad the remaining length with trailing zeros
        for (int i = 0; i < zeros; i++) {
            sb.append('0');
        }
        
        return sb.toString();
    }
}
