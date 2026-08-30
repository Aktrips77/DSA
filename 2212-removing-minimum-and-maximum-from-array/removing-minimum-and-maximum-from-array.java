class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n;

        int minIdx = 0;
        int maxIdx = 0;

        // Locate min and max positions in a single linear scan
        for (int k = 1; k < n; k++) {
            if (nums[k] < nums[minIdx]) minIdx = k;
            if (nums[k] > nums[maxIdx]) maxIdx = k;
        }

        int i = Math.min(minIdx, maxIdx);
        int j = Math.max(minIdx, maxIdx);

        int opt1 = j + 1;
        int opt2 = n - i;
        int opt3 = (i + 1) + (n - j);

        return Math.min(opt1, Math.min(opt2, opt3));
    }
}
