class Solution {
    int avg(int [] arr,int k,int threshold){
        int sum=0;
        int count =0; 
        int targetSum = k * threshold; // Convert average check to sum check to avoid floating-point issues
        // first window  
        for(int i=0;i<k;i++){
            sum+=arr[i];
        }
        if(sum>= targetSum){
            count++;
        }
        
        //sliding window
        for(int j=k;j<arr.length;j++){
            sum=sum-arr[j-k]+arr[j];

        if(sum>=targetSum){
            count++;
        }
        }

        return count;
    }
    public int numOfSubarrays(int[] arr, int k, int threshold) {
       return avg(arr, k, threshold);
    }
}