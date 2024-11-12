class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {} #nums as keys, indices as values, num: index

        for i, num in enumerate(nums): #loop through the nums
            if target - num in hashtable: #calculating which number we need to add to get target
                return [hashtable[target - num], i] #if target - num is found, return the index

            hashtable[num] = i #if "complement" not found, store the current number into table

        return[] #if there is no solution, return empty list
