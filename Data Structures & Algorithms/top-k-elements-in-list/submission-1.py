class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = [[] for i in range(len(nums)+1)]
        countMap = {}

        for i in nums:
            countMap[i]=countMap.get(i,0)+1
        for key,val in countMap.items():
            freq[val].append(key)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
