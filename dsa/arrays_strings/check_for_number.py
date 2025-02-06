def check_for_number(nums: list[int], target: int) -> bool:
    
    count = {}
    for i in range(len(nums)):
        count[nums[i]] = i
    list_keys = list(count.keys())
    for key in list_keys:
        if (target - key) in list_keys:
            return [count[key],count[target-key]]


if __name__=="__main__":
    nums = [1,2,4,5,3,10,56,12]
    target = 6
    print(check_for_number(nums,target))