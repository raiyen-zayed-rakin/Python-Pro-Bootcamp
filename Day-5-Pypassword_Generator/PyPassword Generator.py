# my solve

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

stuff = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letter = int(input())
print("How many symbols would you like in your password?")
symbol = int(input())
print("How many numbers would you like in your password?")
number = int(input())

password = ""
l = 0
n = 0
s = 0
for n in range(1, letter+symbol+number+1):
    if l >= letter:
        stuff = [symbols, numbers]
    elif s >= symbol:
        stuff = [letters, numbers]
    if n >= number:
        stuff = [symbols, letters]
    random_list = random.choice(stuff)
    password += random.choice(random_list)
    if random_list == letters:
        l += 1
    elif random_list == numbers:
        n += 1
    elif random_list == symbols:
        s += 1

print(password)