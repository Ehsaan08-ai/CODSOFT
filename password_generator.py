import random

chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*_"

length = int(input("Enter length of your password: "))
password = ""

for x in range(length):
    password += random.choice(chars)

print()
print(f"Your generated password is :{password}")