print("This is palindrome check")
word = input("please enter a string, and I'm check if it is a palindrome \n")

# print("Is Palindrome? ", word == word[::-1])

rev = ''
for l in reversed(word):
    rev = rev + l

plaindrome = word == rev
print("Is Palindrom? ", plaindrome)