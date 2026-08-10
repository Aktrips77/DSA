class Solution {
    public int romanToInt(String s) {
        int ans = 0, num = 0;
    
    // 1. Traverse the string backwards
    for (int i = s.length() - 1; i >= 0; i--) {
        // 2. Map the current Roman character to its integer value
        switch(s.charAt(i)) {
            case 'I': num = 1; break;
            case 'V': num = 5; break;
            case 'X': num = 10; break;
            case 'L': num = 50; break;
            case 'C': num = 100; break;
            case 'D': num = 500; break;
            case 'M': num = 1000; break;
        }
        
        // 3. Determine if the value should be added or subtracted
        if (4 * num < ans) 
            ans -= num;
        else 
            ans += num;
    }
    return ans;
    }
}