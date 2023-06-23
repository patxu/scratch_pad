def reverseString(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0]

print(reverseString("hello"))