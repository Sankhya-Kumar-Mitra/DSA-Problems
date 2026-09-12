class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l,r = 0,len(heights)-1
        leftMax = heights[0]
        rightMax = heights[r]
        finalResult = 0
        while l<r:
            if leftMax< rightMax:
                l+=1
                leftMax = max(leftMax,heights[l])
                finalResult+= leftMax-heights[l]
            else:
                r-=1
                rightMax = max(rightMax,heights[r])
                finalResult+=rightMax-heights[r]
        return finalResult