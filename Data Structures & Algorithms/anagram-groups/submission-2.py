class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        result = []
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in sortedMap.keys():
                sortedMap[temp]=[]
            sortedMap[temp].append(i)
        for key,val in sortedMap.items():
            result.append(val)
        return result
