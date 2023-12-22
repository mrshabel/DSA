# Maximum Product of Two Elements in an Array

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. Return the maximum value of `(nums[i] - 1) * (nums[j] - 1)`.

## Problem Description

The array-form of an integer `num` is an array representing its digits in left-to-right order.

For example, for `num = 1321`, the array form is `[1, 3, 2, 1]`.

Given `num`, the array-form of an integer, and an integer `k`, this program returns the array-form of the integer `num + k`.

### Example

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose indices 1 and 2 (0-indexed) and subtract 1 from each, you get (nums[1]-1) _ (nums[2]-1) = 3 _ 4 = 12.
