def max_avg(nums: list[int],k: int) -> int:

    sum = 0
    for i in range(k):
        sum += nums[i]
    avg = sum / float(k)

    for i in range(k,len(nums)):
        sum += nums[i] - nums[k-i]
        avg = max(avg, sum / float(k))

    return avg

if __name__=="__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(max_avg(nums,k))

