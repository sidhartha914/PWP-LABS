def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
def is_palindrome(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
def contains_only_digits(s):
    return s.isdigit()

string = input("Enter a string: ")
if contains_only_digits(string):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

sentence = input("Enter a sentence: ")
print("The longest word is:", longest_word(sentence))
def length_of_last_word(sentence):
    words = sentence.strip().split()
    if words:
        return len(words[-1])
    else:
        return 0

sentence = input("Enter a sentence: ")
print("Length of the last word:", length_of_last_word(sentence))
