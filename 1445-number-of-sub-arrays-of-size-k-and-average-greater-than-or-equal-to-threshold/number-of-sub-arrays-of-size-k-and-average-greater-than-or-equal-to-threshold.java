class Solution {

    int avg(int[] arr, int k, int threshold)
    {
        int sum = 0;
        int count = 0;

        // First Window
        for(int i = 0; i < k; i++)
        {
            sum += arr[i];
        }

        if((double)sum / k >= threshold)
        {
            count++;
        }

        // Sliding Window
        for(int j = k; j < arr.length; j++)
        {
            sum = sum - arr[j-k] + arr[j];

            if((double)sum / k >= threshold)
            {
                count++;
            }
        }

        return count;
    }

    public int numOfSubarrays(int[] arr, int k, int threshold)
    {
        return avg(arr, k, threshold);
    }
}