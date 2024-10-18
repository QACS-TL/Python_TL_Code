def add_numbers(a, b):
    return a + b

# Test the function
result = add_numbers(10, 20)
print("The sum is:", result)


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if string is the same forward and backward
    return s == s[::-1]

# Test the function
string = "madam"
print(string, "is a palindrome:", is_palindrome(string))

string = "hello"
print(string, "is a palindrome:", is_palindrome(string))