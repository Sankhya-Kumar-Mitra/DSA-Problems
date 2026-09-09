class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        int l = nums.length;
        Arrays.sort(nums);
        for (int i=0;i<l-1;i++){
            if (nums[i]==nums[i+1]){
                return true;
            }
        }

        return false;
    }
}