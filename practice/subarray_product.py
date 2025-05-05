
def subarray_product(nums: list[int], k: int) -> int:

    left = count = 0
    product = 1
    for right in range(len(nums)):
        product *= nums[right]
        if product >= k:
            product //= nums[left]
            left += 1
            count += right - left + 1
        else:
            count += right -left + 1

    return count

        

 

if __name__=="__main__":

    nums = [10, 5, 2, 6]
    k = 100
    print(subarray_product(nums,k))
