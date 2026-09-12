class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left , right = 1,max(piles)-1
        result = 0

        while left <= right:
            mid = left+ (right-left)//2
            curHour = 0
            
            for i in range(len(piles)):
                curHour += math.ceil(float(piles[i])/mid) 
                
            if curHour <= h:
                right = mid-1
            else:
                left = mid+1
        return left

        