def is_palindrome(word: str):
    """
    Prints true or false depends on 
    if the given word argument is a palindrome or not
    """
    if word.isalnum():
        return word.lower() == word.lower() [:: -1] 
    else:
        return False
       
print(is_palindrome("Potop"))
print(is_palindrome("nos"))
print(is_palindrome("kaJaK"))
print(is_palindrome("brat"))