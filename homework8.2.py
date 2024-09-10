def is_palindrome(text:str):
    new_text = ""
    for letter in text:
        if letter.isalpha() or letter.isdigit():
            new_text += letter.upper()
    if new_text == new_text[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")