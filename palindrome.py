def is_palindrome(word):
    """
    Prints true or false depends on 
    if the given word argument is a palindrome or not
    """
    if word == word[:: -1]:
        return True
    else:
        return False
    
print(is_palindrome("potop"))
print(is_palindrome("nos"))
print(is_palindrome("kajak"))
print(is_palindrome("brat"))