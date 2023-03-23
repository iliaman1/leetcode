def is_palindrome(s: str) -> bool:
    s = s.lower()
    for character in ' !@#$%^&*()_+=,./?|:;[]{}\\\"\'-`':
        while character in s:
            s = s.replace(character, '')
    if len(s) == 0:
        return True
    elif s == s[::-1]:
        return True
    else:
        return False
