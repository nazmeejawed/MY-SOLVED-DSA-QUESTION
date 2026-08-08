class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)

        # Build prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = 0

        # Generate all subarrays
        for left in range(n):
            for right in range(left, n):

                length = right - left + 1

                # Only odd-length subarrays
                if length % 2 == 1:

                    # Get subarray sum using prefix sum
                    total += prefix[right + 1] - prefix[left]

        return total