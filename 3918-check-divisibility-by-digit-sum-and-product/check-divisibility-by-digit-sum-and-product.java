class Solution {
    public boolean checkDivisibility(int n) {
        int sum=0;
        int product=1;
        int temp=n ; // n ki value fix rehni chahiye end me isiliye temp se while me kaam karo taaki temp 0 HO n nahi

        while(temp>0){
            int rem=temp%10;
            sum+=rem;
            product*=rem;
            temp= temp/ 10;  // yeh truncate krke n ki value kam hoti rahegi
        }

        int total=sum+product; //question condition 

        return n % total ==0; // bool return
    }
}