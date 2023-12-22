class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        temp = [0, 0]
        for i in nums:
            if i > temp[0]:
                temp[0] = i
            elif i > temp[1]:
                temp[1] = i
        print(temp)
        return (temp[0] - 1)*(temp[1] - 1)

   
response = Solution()
answer = response.maxProduct([3,4,5,2])

print(answer)