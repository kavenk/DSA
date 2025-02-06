"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

"""

def reverse_words(s: str) -> str:
    t = s.split()
    new_s = ""
    for word in t:
        new_s += word[::-1]
        new_s += " "
    return "".join(new_s).strip()

if __name__=="__main__":
    s = "Let's take LeetCode contest"
    print(reverse_words(s))


