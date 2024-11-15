import zipfile
import itertools
import string
import tkinter as tk
from tkinter import filedialog

zip_file_path = filedialog.askopenfilename(filetypes=(('ZIP files', '*.zip*'),))

option = int(input("Select Password Type\n--------------------------\n1. Numbers\n2. Uppercase\n3. Lowercase\n4. All\n--------------------------\nOption : "))
print(f"Selected Option : {option}")

if option == 1:
    characters = string.digits
elif option == 2:
    characters = string.ascii_uppercase
elif option == 3:
    characters = string.ascii_lowercase
elif option == 4:
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase


min_length = 1
max_length = 5

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f"Password Founded : {password}")
        return True
    except:
        return False
    
with zipfile.ZipFile(zip_file_path) as zf:
    found = False
    for length in range(min_length, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            print(f"trying password... : {password}")
            if extract_zip(zf, password):
                found = True
                break
        if found:
            break

    else :
        print("Failed to find Password...")