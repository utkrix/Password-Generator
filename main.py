import random
import string
import pyperclip
from tkinter import *

# PASSWORD CHARACTERISTICS
alphabets = string.ascii_letters
num = string.digits
symbols = string.punctuation

print("Welcome to Password Generator with Python! Enter 0000 to quit the program.")
# Loop to not terminate until user enters "000"
while True:
        # User Pasword length
        length = int(input("Enter the length of the the password in number form! \n>"))
        # Generating Password:
        if length != 0000:
            generated = alphabets + num + symbols
            temp = random.sample(generated,length)
            #create the password 
            password = "".join(temp)
            # copying password to clip board!
            pyperclip.copy(password)
            spam = pyperclip.paste()
            print(f"Your generated password is:\n{password} \nIt has also been copied to your clipboard!")
        else:
            print("Thank you for using Password Generator. Be safe out there 👀")
            break


