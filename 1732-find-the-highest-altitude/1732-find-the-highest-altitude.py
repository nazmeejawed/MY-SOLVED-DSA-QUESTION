class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        maximum = 0
        
        for num in gain:
            current += num
            maximum = max(maximum,current)
        
        return maximum
        
        