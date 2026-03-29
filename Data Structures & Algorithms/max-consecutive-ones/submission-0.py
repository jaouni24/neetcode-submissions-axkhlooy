class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        max_value = 0
        for i in nums:
            if i == 1:
                counter +=1

            if counter > max_value:
                max_value = counter

            if i == 0:
                counter = 0

        return max_value