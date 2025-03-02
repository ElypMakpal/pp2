#  Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if __name__ == "__main__":
    generate_files()