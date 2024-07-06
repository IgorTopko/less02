def is_palindrome(text):
    good_text = ''.join(ch.lower() for ch in text if ch.isalnum())
    return good_text == good_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")