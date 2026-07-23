class Solution {
    public int maxArea(int[] height) {
        // hamesha choti height waale pointer ko move karenge 

        int left =0;
        int right=height.length-1;
        int Maxarea=0; // maximum area return karna hain

        while(left<right){
            // area calculate karenge
            int area=Math.min(height[left],height[right]) * (right-left) ; // area= height * width aur minimum isiliye ki height slope chota hoga toh paani zyada aayega

            Maxarea=Math.max(Maxarea,area);

            // agar left ki height choti toh usse front move krnege
            if(height[left]<height[right]){
                left ++;
            }
            else{
                right--;
            }


        }

        return Maxarea;
    }
}