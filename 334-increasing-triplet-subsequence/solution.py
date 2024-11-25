class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        smallest = float('inf')
        larger = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= larger:
                larger = num
            else:
                return True

        return False
