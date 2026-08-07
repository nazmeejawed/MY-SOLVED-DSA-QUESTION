class Solution(object):
    def thirdMax(self, nums):
        largest = float("-inf")
        second_largest = float("-inf")
        third_largest = float("-inf")

        for num in nums:

            # Duplicate skip
            if num == largest or num == second_largest or num == third_largest:
                continue

            if num > largest:
                third_largest = second_largest
                second_largest = largest
                largest = num

            elif num > second_largest:
                third_largest = second_largest
                second_largest = num

            elif num > third_largest:
                third_largest = num

        if third_largest == float("-inf"):
            return largest

        return third_largest