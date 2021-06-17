class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        outList = []

        for i in range(len(nums)):
            outList.append(nums.count(nums[i]))

        for j in range(len(outList)):
            if outList[j] == 1:
                return nums[j]