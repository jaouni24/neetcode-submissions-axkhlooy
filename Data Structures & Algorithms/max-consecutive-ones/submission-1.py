class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        max_value = 0
        for i in nums:
            if i == 0:
                max_value = max(counter, max_value)
                counter = 0

            else:
                counter += 1

        return max(counter, max_value)