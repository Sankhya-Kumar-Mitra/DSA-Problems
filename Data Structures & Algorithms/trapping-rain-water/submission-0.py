class Solution:
    def trap(self, heights: List[int]) -> int:
        l = len(heights)
        rightMax = [0]*l
        leftMax = [0]*l
        finalResult = 0
        lVal = heights[0]
        rVal = heights[l-1]
        for i in range(l):
            if i ==0:
                leftMax[i]=0
            else:
                if heights[i]>lVal:
                    leftMax[i] = lVal
                    lVal = heights[i]
                else:
                    leftMax[i] = lVal
        
        for i in range(l-1,0,-1):
            if i ==(l-1):
                rightMax[i] = 0
            else:
                if heights[i]>rVal:
                    rightMax[i] = rVal
                    rVal = heights[i]
                else:
                    rightMax[i] = rVal

        for i in range(l):
            if i==0 or i == l-1:
                continue
            if leftMax[i]>heights[i] and rightMax[i]>heights[i]:
                finalResult+= min(leftMax[i],rightMax[i]) - heights[i]

                
        return finalResult