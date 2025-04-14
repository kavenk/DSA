
def char_to_appear_twice(s: str) -> str:
    
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
            return char
        else:
            frequency[char] = 1
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return None  # Return None if no character appears twice

# Example usage
if __name__=="__main__":
    s = "bcabca"
    print(char_to_appear_twice(s))