class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ''.join([c for c in s if c.isalnum()])
        l = len(newS)
        i=0
        j=l-1   
        while i<=j:
            if newS[i]!=newS[j]:
                return False
            i+=1
            j-=1
        return True