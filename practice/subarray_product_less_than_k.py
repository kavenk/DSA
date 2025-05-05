
def subarray_less_than_k(nums: list[int],k :int) -> int:

    product = 1

    left = 0
    count = 0
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k and left <= right:
            product /= nums[left]
            left += 1
        count += right - left + 1

    return count


nums = [10,5,2,6]
k = 100
print(subarray_less_than_k(nums,k))

