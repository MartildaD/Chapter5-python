words = ['level', 'world', 'madam', 'python']

def is_palindrome(word):
    return word == word[::-1]

palindromes = list(filter(is_palindrome, words))
print(palindromes)
