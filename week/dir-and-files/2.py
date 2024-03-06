#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

# path = input()
path = "./3.py"
print("Existence:", os.access(path, os.F_OK))
print("Readability:", os.access(path, os.R_OK))
print("Writeability:", os.access(path, os.W_OK))
print("Executeability:", os.access(path, os.X_OK))