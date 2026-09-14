class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicateSet = set()
        j=0
        length=0
        result=0
        for i in range(len(s)):
            if s[i] not in duplicateSet:
                duplicateSet.add(s[i])
                length+=1
            else:
                
                length+=1
                while s[j]!=s[i]:
                    duplicateSet.remove(s[j])
                    j+=1
                    length-=1
                duplicateSet.remove(s[j])
                j+=1
                length-=1
                
                duplicateSet.add(s[i])
            result = max(length,result)
        return result