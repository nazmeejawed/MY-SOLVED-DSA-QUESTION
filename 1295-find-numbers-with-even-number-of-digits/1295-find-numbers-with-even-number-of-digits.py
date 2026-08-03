class Solution(object):
    def findNumbers(self, nums):
        answer = 0
        for i in range(len(nums)):
            number = nums[i]
            digit_count = 0
            while number > 0:
                digit_count += 1
                number //= 10
            if digit_count % 2 == 0:
                    answer += 1
        return answer
    
            
       