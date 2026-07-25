class Solution {
    public int maxProduct(int n) {
        int largest = 0;
        int secondLargest = 0;

        // एक-एक करके पीछे से सारी डिजिट्स निकालें
        while (n > 0) {
            int currentDigit = n % 10;

            if (currentDigit > largest) {
                // अगर करंट डिजिट सबसे बड़ी है, तो पुरानी सबसे बड़ी अब दूसरी सबसे बड़ी बन जाएगी
                secondLargest = largest;
                largest = currentDigit;
            } else if (currentDigit > secondLargest) {
                // अगर करंट डिजिट सिर्फ दूसरी सबसे बड़ी से बड़ी है
                secondLargest = currentDigit;
            }

            n /= 10; // आखरी डिजिट को हटा दें
        }

        // दोनों सबसे बड़ी डिजिट्स का गुणा रिटर्न करें
        return largest * secondLargest;
    }
}
