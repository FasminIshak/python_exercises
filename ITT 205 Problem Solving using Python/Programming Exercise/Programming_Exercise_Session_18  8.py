def palindrome(str):
    rev = ''.join(reversed(s))
    if (s == rev):
        return "palindrome"
    return "Not palindrome"