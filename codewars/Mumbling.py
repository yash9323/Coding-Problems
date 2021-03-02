"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(s):
    ans=""
    for i in range(len(s)):
        ans+=s[i].upper()
        for j in range(i):
            ans+=s[i].lower()
        if i < len(s)-1:
            ans=ans+'-'
    return ans
             
