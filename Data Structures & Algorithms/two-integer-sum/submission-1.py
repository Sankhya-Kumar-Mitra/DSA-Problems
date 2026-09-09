class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_map = {}

        for i in range(len(nums)):
            if (target-nums[i]) in temp_map.keys():
                result.append(temp_map[target-nums[i]])
                result.append(i)
            temp_map[nums[i]] = i

        return result