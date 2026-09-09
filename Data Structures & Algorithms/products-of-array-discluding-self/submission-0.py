class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lp = [1]*l
        rp = [1]*l
        lp[0] = nums[0]
        rp[-1] = nums[-1]

        result = []
        
        for i in range(1,len(nums)):
            lp[i]=lp[i-1]*nums[i]
            rp[l-1-i]= rp[l-i]*nums[l-1-i]
        
        for i in range(l):
            if i==0:
                result.append(rp[i+1])
            elif i==l-1:
                result.append(lp[i-1])
            else:
                result.append(lp[i-1]*rp[i+1])
        return result