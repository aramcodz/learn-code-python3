import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy/ Simple Version
letters = random.sample(letters, nr_letters - nr_numbers - nr_symbols)
symbols = random.sample(symbols, nr_symbols)
numbers = random.sample(numbers, nr_numbers)
new_pw_lst = letters + symbols + numbers
simple_password = "".join(new_pw_lst)
print("Your simple/ordered password is: " + simple_password)

# Add more randomness (char order) to password
random.shuffle(new_pw_lst)
new_password = "".join(new_pw_lst)

print("Your random ordered password is: " + new_password)