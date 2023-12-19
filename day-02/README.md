# Power of Two Checker

This code checks if a given number is a power of 2, returning `true` if it is and `false` otherwise.

## Runtime Analysis

### Method 1: `isPowerofTwo1`

#### This method uses branching statements to check for false conditions before checking for the truthful ones

- Runtime: `6953ms` on Leetcode

### Method 2: `isPowerofTwo2`

#### This method relies on the fact that a number is a power of 2 if and only if it has a single bit of 1 in its binary bit representation. Thus, 2 = 0001, 4 = 0010, 8 = 0100... and the integers before them have alternating bits as opposed to the powers of 2 above. It then uses the bitwise operator to compare the bits of `n` and `n-1`.

-Eg. 16 = 1000, (16 - 1 = 15) = 0111. 16 & 15 = 0000. Thus, 16 is a power of 2.

- Runtime: `23ms` on Leetcode
