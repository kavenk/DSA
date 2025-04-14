
def find_numbers(nums: list[int]) -> list[int]:
    nums = set(nums)
    result = []
    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            result.append(num)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_numbers(nums))
    # Output: []
    nums = [1, 3, 5, 7, 9]
    print(find_numbers(nums))
    # Output: [1, 3, 5, 7, 9]
    nums = [1, 2, 4, 6, 8]
    print(find_numbers(nums))

    

            