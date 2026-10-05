class Solution {
    public int scoreOfParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(0); // Base score frame
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(0); // Start a new inner frame
            } else {
                int innerScore = stack.pop();
                int outerScore = stack.pop();
                // If innerScore is 0, it was (), so score is 1. Otherwise, 2 * innerScore.
                stack.push(outerScore + Math.max(2 * innerScore, 1));
            }
        }
        
        return stack.pop();
    }
}