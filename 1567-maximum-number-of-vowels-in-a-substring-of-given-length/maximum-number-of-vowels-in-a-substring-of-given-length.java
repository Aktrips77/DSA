class Solution {
    public boolean isVowel(char ch){
        return  ch=='a' || ch=='e' || ch=='i'|| ch=='o' || ch=='u';
           
    }
    public int maxVowels(String s, int k) {
        int Currentcount=0;
        // first window
        for(int i=0; i<k;i++){
            if(isVowel(s.charAt(i))){
            Currentcount++;
            }
        }
        int maxcount=Currentcount;

        for(int j=k;j<s.length();j++){
            if(isVowel(s.charAt(j))){
                Currentcount++;
            }
            if(isVowel(s.charAt(j-k))){
                Currentcount--; // window ke piche se vowel count hata raha yeh array nh hain toh string me aise hota hain
            }

            maxcount=Math.max(maxcount,Currentcount);
        }
    
            
      return maxcount;
        
    }
}