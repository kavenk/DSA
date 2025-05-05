def sorted_array(nums1: list[int], nums2: list[int]) -> list[int]:

    i = j = 0
    new_array = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            new_array.append(nums1[i])
            i += 1
        else:
            new_array.append(nums2[j])
            j += 1

    while i < len(nums1):
        new_array.append(nums1[i])
        i += 1
    while j < len(nums2):
        new_array.append(nums2[j])
        j += 1

    return new_array

if __name__=="__main__":
    nums1 = [1,4,7,20]
    nums2 = [3,5,6]
    print(sorted_array(nums1,nums2))