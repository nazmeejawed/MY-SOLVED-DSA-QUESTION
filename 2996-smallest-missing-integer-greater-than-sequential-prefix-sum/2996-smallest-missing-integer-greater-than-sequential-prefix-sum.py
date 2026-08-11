class Solution:
    def missingInteger(self, nums):
        # Step 1: Calculate sum of the longest sequential prefix
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
            
        # Step 2: Find the smallest integer >= prefix_sum not present in nums
        num_set = set(nums)
        x = prefix_sum
        while x in num_set:
            x += 1
            
        return x