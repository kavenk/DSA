
def counting_elements(arr: list[int]) -> list[int]:
    
    arr_set = set(arr)
    count = 0
    for num in arr:
        if num +1 in arr_set:
            count += 1
    return count

if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5]
    result = counting_elements(arr)
    print(f"The count of elements that have a successor in the array is: {result}")