class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                    return [i, j]
                
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
                
numbers = TwoSum()
numbers1 = numbers.twoSum([3, 2, 4], 6)
numbers2 = numbers.twoSum1([3, 2, 4], 6)

print(f"The results for numbers1 are {numbers1}.\nThe results for numbers2 are {numbers2}.")