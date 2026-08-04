class Solution(object):
    def getConcatenation(self, nums):
        result = []

        for i in range(2 * len(nums)):
            result.append(nums[i % len(nums)])

        return result