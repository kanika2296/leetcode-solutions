class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        o = []
        for i in range(0,n):
            o.append(nums[i])
            o.append(nums[i+n])
        return o
