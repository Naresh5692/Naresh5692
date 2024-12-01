def is_palindrome(number):
    return number == number[::-1]
number =input("Enter a number:")
if is_palindrome(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome!")