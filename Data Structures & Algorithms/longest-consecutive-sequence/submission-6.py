class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in numSet:
                length = 0
                current=i
                while current in numSet:
                    length+=1
                    current+=1
                longest = max(longest,length)

        return longest
