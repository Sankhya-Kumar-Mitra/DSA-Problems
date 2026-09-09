class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        countMap = {}
        result = []
        for i in nums:
            countMap[i] = countMap.get(i,0)+1

        for key,val in countMap.items():
            heapq.heappush(heap,(-val,key))
        
        for i in range(k):
            current = heapq.heappop(heap)
            result.append(current[1])

        return result
