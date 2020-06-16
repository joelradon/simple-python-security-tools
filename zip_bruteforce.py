import zipfile
from tqdm import tqdm
import zipfile
import sys
import os

# the password list path you want to use
wordlist = "top_1000_passwords.txt"
# the zip file you want to crack its password
zip_file = input("Enter zip file location: ")
if os.path.isdir(zip_file):
    f = open(zip_file, "r+")
else:
    print ("Directory not exists.")
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
