class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        result = []
        while i<j:
            if nums[i]+nums[j]==target:
                result.append(i+1)
                result.append(j+1)
                break
            elif nums[i]+nums[j] < target:
                i+=1
            else:
                j-=1
        return result