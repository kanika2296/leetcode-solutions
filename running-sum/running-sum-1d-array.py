
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        o = []
        o.append(nums[0])
        for i in range(1,len(nums)):
            o.append(o[i-1]+nums[i]);
        return o
   
