import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> [int]:
        final = int("".join(map(str, num))) + k

        output = [int(digit) for digit in str(final)]
        return output
        
response = Solution()
answer = response.addToArrayForm([7,8,2,9,2,8,0,4,1,6,5,8,2,7,7,4,3,6,6], 312)

print(answer)