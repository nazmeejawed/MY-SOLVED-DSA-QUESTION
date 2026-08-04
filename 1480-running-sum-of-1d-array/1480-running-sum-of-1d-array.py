class Solution:
    def runningSum(self,nums):
        total = 0
        result = []
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result