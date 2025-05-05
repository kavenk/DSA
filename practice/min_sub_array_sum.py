def min_size_subarray(nums: list[int], target: int) -> int:
    sum = 0
    left = 0
    size_sub = float("inf")
    for right in range(len(nums)):
        sum += nums[right]
        while sum > target:
            sum -= nums[left]
            left += 1
            size_sub = min(size_sub, right - left + 1)
    return size_sub if size_sub != float("inf") else 0

if __name__=="__main__":
    target = 4
    nums = [1,4,4]
    print(min_size_subarray(nums,target))


