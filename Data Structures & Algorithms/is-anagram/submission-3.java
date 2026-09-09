class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()){
            return false;
        }
        Map<Character,Integer> firstWord = new HashMap<>();
        Map<Character,Integer> secondWord = new HashMap<>();

        for (int i = 0;i<s.length();i++){
            firstWord.put(s.charAt(i),firstWord.getOrDefault(s.charAt(i),0)+1);
            secondWord.put(t.charAt(i),secondWord.getOrDefault(t.charAt(i),0)+1);
        }
        return firstWord.equals(secondWord);
        
    }
}
