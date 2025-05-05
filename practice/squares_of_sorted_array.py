def squares_of_sorted(nums: list[int]) -> list[int]:
    i = 0
    j = len(nums) - 1
    sorted_array = [0]*len(nums)
    k = len(nums) - 1
    while i <= j:

        if abs(nums[i]) <= abs(nums[j]):
            sorted_array[k] = nums[j]**2
            j -= 1
            k -= 1
        else:
            sorted_array[k] = nums[i]**2
            i += 1
            k -= 1

    return sorted_array

if __name__=="__main__":
    nums = [-7,-3,2,3,11]
    print(squares_of_sorted(nums))