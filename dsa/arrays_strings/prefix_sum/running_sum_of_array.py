"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

def running_sum(nums):
    prefix = [nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i] + prefix[i-1])

    return prefix

if __name__=="__main__":
    nums = [3,1,2,10,1]
    print(running_sum(nums))

