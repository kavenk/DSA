"""
Reverse Only Letters
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

def reverse_only_letters(s: str) -> str:
    letters = [c for c in s if c.isalpha()]
    ans = []
    for c in s:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return "".join(ans)



if __name__=="__main__":
    s = "Test1ng-Leet=code-Q!"
    print(reverse_only_letters(s))