class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        l = len(temp)
        result = [0]*l
        
        for i in range(1,len(temp)):
            while len(stack) >0 and temp[i]>temp[stack[-1]]:
                result[stack[-1]] = i-stack[-1]
                stack.pop(-1)

            stack.append(i) 
        
        return result