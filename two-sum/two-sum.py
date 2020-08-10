class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0,len(nums)):
            d = target-nums[i]
            if d in m:
                return {i,m[d]}
            else:
                m[nums[i]]=i
        
