class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        l1,l2 = len(s1),len(s2)
        l,r = 0,l1
        s1Map = {}
        for i in s1:
            s1Map[i]=s1Map.get(i,0)+1

        while r<=l2:
            s2Map = {}
            for i in s2[l:r]:
                s2Map[i] = s2Map.get(i,0)+1
            if s2Map == s1Map:
                return True
            l+=1
            r+=1
        return False
            
