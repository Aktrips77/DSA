class Solution {
    public int totalNumbers(int[] digits) {
       
        // set to store unique numbers 
        HashSet<Integer> uniqueNum= new HashSet<>();

        int n= digits.length;
        // i=hundreeds places j= tens place k= ones place
        for(int i=0;i<n;i++){
            // condition me leading 0 allowed nahi hain 
            if(digits[i]==0) continue;

            for(int j=0;j<n;j++){
                // ek number/index ko dobara use nahi karte
                if(i==j) continue;

                for( int k=0;k<n;k++){
                    // 3rd index 1st aur 2nd ke equal nahi honi chahiye 
                    if( i==k || j==k) continue;

                    // number should be even 
                    if(digits[k]%2==0){
                        // 3 digits ko combine 
                        int num=digits[i]*100 + digits[j]*10+ digits[k]*1;
                        uniqueNum.add(num);
                    }
                }
            }
        } // size return karna hain ki numbers kitne hain
         return uniqueNum.size();
    }
}