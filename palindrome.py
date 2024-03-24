def is_palindrome(expression: str):
    """
    Prints true or false depends on 
    if the given word argument is a palindrome or not
    """
    word = ""
    for char in expression:
        if char.isalnum():
            word = word + char
    if word.lower() == word.lower() [:: -1]:
        return True
    else:
        return False
       
print(is_palindrome("Kobyła ma mały bok!"))
print(is_palindrome("nos"))
print(is_palindrome("kaJaK?"))
print(is_palindrome("brat"))