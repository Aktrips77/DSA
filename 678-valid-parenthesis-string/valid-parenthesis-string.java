class Solution {
    public boolean checkValidString(String s) {
        int cmin = 0;
        int cmax = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                cmin++;
                cmax++;
            } else if (c == ')') {
                cmin--;
                cmax--;
            } else if (c == '*') {
                cmin--; // treated as ')'
                cmax++; // treated as '('
            }
            
            if (cmax < 0) return false;
            cmin = Math.max(cmin, 0);
        }
        
        return cmin == 0;
    }
}
