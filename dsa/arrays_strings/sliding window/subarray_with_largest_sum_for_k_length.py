"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""

def subarray_largest_sum(nums,k):
    curr_sum = 0
    for i in range(k):
        curr_sum += nums[i]
    ans = curr_sum
    for i in range(k,len(nums)):
        curr_sum += nums[i] - nums[i - k]
        ans = max(ans,curr_sum)
    return ans


if __name__=="__main__":
    nums = [3,-1,4,12,-8,5,6]
    k = 4

    print(subarray_largest_sum(nums,k))