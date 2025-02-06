"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
def sorted_array(arr):
    length = len(arr) - 1
    l = 0
    r = length
    sorted_array = [0] * len(arr)
    for i in range (length, -1, -1):
        if abs(arr[l]) < abs(arr[r]):
            num = arr[r]
            r -= 1
        else:
            num = arr[l]
            l += 1
        sorted_array[i] = num * num
    return sorted_array



if __name__=="__main__":
    arr1 = [-8,-4,-1,0,3,10]
    arr2 = [-2,-1,0,1,2,3]
    print(sorted_array(arr2))




