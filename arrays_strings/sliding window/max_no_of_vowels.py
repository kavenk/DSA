
def max_no_of_vowels(s: str, k: int)-> int:
    vowel = "aeiou"
    count = 0
    max_count = 0
    for i in range(k):
        if s[i] in vowel:
            count += 1
    max_count = count
    for i in range(k, len(s)):
        if s[i] in vowel:
            count += 1
        if s[i - k] in vowel:
            count -= 1
        max_count = max(max_count,count)
    return max_count
if __name__=="__main__":
    s = "leetcode"
    k = 3
    print(max_no_of_vowels(s,k))


