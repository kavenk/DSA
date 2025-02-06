"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]

"""

def maximum_consec_ones(nums,k):
    left = 0
    ones = 0
    count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            ones += 1
        while ones > k:
            if nums[left] == 0:
                ones -= 1
            left += 1
        count = max(count, right - left + 1)
    return count

if __name__=="__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(maximum_consec_ones(nums, k))

