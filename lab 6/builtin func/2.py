# Write a Python program with builtin function that accepts a string 
# and calculate the number of upper case letters and lower case letters
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())  # Count uppercase letters
    lower_count = sum(1 for char in s if char.islower())  # Count lowercase letters
    return upper_count, lower_count

# Example usage
text = input("Enter a string: ")
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
