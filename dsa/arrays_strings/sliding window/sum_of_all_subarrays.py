"""
Given an integer array arr[], find the sum of all sub-arrays of the given array. 

Examples: 

Input: arr[] = [1, 2, 3]
Output: 20
Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20


Input: arr[] = [1, 2, 3, 4]
Output: 50
"""

def sum_of_all_subarrays(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i] * (i + 1) * (len(nums) - i)
    return sum


if __name__=="__main__":
    nums = [1, 2, 3, 4]
    print(sum_of_all_subarrays(nums))
