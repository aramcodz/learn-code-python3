import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy/ Simple Version using lists and range
new_password = ""
for char in range(0, nr_letters):
    new_password += random.choice(letters)

for char in range(0, nr_symbols):
    new_password += random.choice(symbols)

for char in range(0, nr_numbers):
    new_password += random.choice(numbers)


# Easy/ Simple Version using random.sample
print("Your simple/ordered password is: " + new_password)

# Add more randomness (char order) to password
new_pw_lst = list(new_password)
random.shuffle(new_pw_lst)
new_password = "".join(new_pw_lst)


print("Your random ordered password is: " + new_password)