#!/usr/bin/env/python3.7
import itertools as it
import string
import sys
print("\nWordlistPuzzle v1.0 by u/Moluma\n")
def count_char(passwd, char):
    count = passwd.count(char)
    return count

file = str(input("Password file name: "))
unknown_char = str(input("Set unknown character (you can use any ascii char): "))
password = str(input("Password structure (ex: P" + unknown_char + "sswor" + unknown_char + "): "))
length = count_char(password, unknown_char)
original_list = []

numbers = str(input("Do you want to use numbers (y/n): "))
if numbers == "y":
    original_list = original_list + list(string.digits)
else:
    pass
lowercase = str(input("Do you want to use lowercase letters (y/n): "))
if lowercase == "y":
    original_list = original_list + list(string.ascii_lowercase)
else:
    pass
uppercase = str(input("Do you want to use upperrcase letters (y/n): "))
if uppercase == "y":
    original_list = original_list + list(string.ascii_uppercase)
else:
    pass
symbols = str(input("Do you want to use symbols (y/n): "))
if symbols == "y":
    original_list = original_list + list(string.punctuation)
    original_list.remove("\\")
else:
    pass
if unknown_char in original_list:
    original_list.remove(unknown_char)
else:
    pass
denychar = str(input("Banned characters (ex: 123abc!$&), (if you don't want to ban any just hit enter): "))
for deniedchar in denychar:
    original_list.remove(deniedchar)
passwd_number = len(original_list)**len(password)
print("\nYou are about to generate a file of " + str(passwd_number) + " passwords.")
r_u_sure = str(input("Do you want to continue? (y/n): "))
if r_u_sure == "y":
    pass
else:
    sys.exit(1)
my_file = open(file, "w")
permutations = it.product(original_list, repeat=length)
for i in permutations:
    guess = ""
    temp = password
    for e in i:
        guess = str(guess) + str(e)
        a = 0
    for t in list(guess):
        temp = temp.replace(unknown_char, str(guess[a]), 1)
        a = a+1
    my_file.write(temp + '\n')
print("\nDone! Saved to " + file + "!")
