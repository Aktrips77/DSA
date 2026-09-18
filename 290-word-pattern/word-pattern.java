import java.util.HashMap;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        // String ko spaces ke basis par words mein split karein
        String[] words = s.split(" ");
        
        // Agar pattern ki length aur words ki sankhya alag hai, toh false
        if (pattern.length() != words.length) {
            return false;
        }
        
        // Character se Word aur Word se Character ki mapping ke liye 2 HashMaps
        HashMap<Character, String> charToWord = new HashMap<>();
        HashMap<String, Character> wordToChar = new HashMap<>();
        
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];
            
            // Check karein agar character pehle se mapped hai
            if (charToWord.containsKey(c)) {
                if (!charToWord.get(c).equals(word)) {
                    return false; // Agar purana mapped word naye word se match nahi karta
                }
            } else {
                charToWord.put(c, word);
            }
            
            // Check karein agar word pehle se kisi character se mapped hai
            if (wordToChar.containsKey(word)) {
                if (wordToChar.get(word) != c) {
                    return false; // Agar purana mapped character naye character se match nahi karta
                }
            } else {
                wordToChar.put(word, c);
            }
        }
        
        return true; // Agar saari conditions satisfy ho jayein
    }
}