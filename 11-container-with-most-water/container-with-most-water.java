class Solution {
    public int maxArea(int[] height) {
        // hamesha choti height waale pointer ko move karaenge 

        int l=0;
        int r= height.length-1;
        int Maxarea=0;

        while(l<r){
            // area calculation 
           int width= r-l;
           int lambai=Math.min(height[l],height[r]);
           int area= lambai * width;

           Maxarea=Math.max(Maxarea,area);

           if(height[l]<height[r]){
            l++;
           }
           else{
            r--;
           }

        }
        return Maxarea;
    }
}