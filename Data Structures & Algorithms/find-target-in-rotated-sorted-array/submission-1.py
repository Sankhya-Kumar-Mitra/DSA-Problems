class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        result = -1
        while l<=r:
            mid = l+(r-l)//2
            print(l)
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid]>= nums[l]:
                if target<=nums[mid] and target >= nums[l]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target >= nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1

        return result