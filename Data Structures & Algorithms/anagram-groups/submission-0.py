class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        sortMap = {}
        for i in strs:
            tempStr = ''.join(sorted(i))
            if tempStr not in sortMap.keys():
                sortMap[tempStr] = []
            sortMap[tempStr].append(i)

        for key,val in sortMap.items():
            result.append(val)

        return result