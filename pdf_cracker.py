import pikepdf
from tqdm import tqdm
import os

pdfname = input('Enter a file name: ')

# load password list
passwords = [ line.strip() for line in open("top_1000_passwords.txt") ]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open(pdfname, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
