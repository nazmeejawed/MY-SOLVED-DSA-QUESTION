class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        # Last digit se start karenge
        for i in range(n - 1, -1, -1):

            # Agar digit 9 se chhoti hai
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # Agar 9 hai to 0 bana do aur carry aage jayega
            digits[i] = 0

        # Agar saare digits 9 the
        return [1] + digits