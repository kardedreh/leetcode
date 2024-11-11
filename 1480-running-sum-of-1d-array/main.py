class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for num in nums:
            sum += num
            result.append(sum)
        return result

solution = Solution()
print(solution.runningSum([1,2,3,4]))
