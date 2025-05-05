def string_sub(s: str, t: str)-> bool:
    i = j = 0
    new_s = ""
    while i < len(s) and j < len(t):

        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return ( i == len(s))


def reverse_words(s: str)-> str:
    s1 = s.split(" ")
    new_s = ""
    for word in s1:
        new_s += word[::-1]
        new_s += " "
    return new_s.strip()
def reverse_only_words(s: str)-> str:
    letters = [c for c in s if c.isalpha()]
    new_s = ""
    for c in s:
        if c.isalpha():
            new_s += letters.pop()
        else:
            new_s += c
    return new_s

def minimum_value(nums1,nums2):
    i = j = 0
    minimum = float("inf")
    while i < len(nums1):
        if nums1[i] in nums2:
            minimum = min(minimum,nums1[i])
        i += 1
    
    if minimum != float("inf"):
        return minimum
    else: 
        return -1


    
def reverse_prefix(word, ch):

    for i in range(len(word)):
        if word[i] == ch:
            return word[i:-1] + word[i+1::]




if __name__=="__main__":
    s = "ace" 
    t = "abcdeee"
    # print(string_sub(s,t))
    s = "Test1ng-Leet=code-Q!"
    ch = '1'
    nums1 = [1,2,3]
    nums2 = [2,4,1]
    print(reverse_prefix(s,ch))

